import datetime
import json
import logging

from django.apps import apps
from django.conf import settings
from django.utils.timezone import now

from mayan.apps.acls.models import AccessControlList

from ..permissions import permission_workflow_instance_transition

logger = logging.getLogger(name=__name__)


class WorkflowInstanceBusinessLogicMixin:
    def check_escalation(self):
        current_state = self.get_current_state()

        for escalation in current_state.escalations.filter(enabled=True):
            kwargs = {escalation.unit: escalation.amount}
            timedelta = datetime.timedelta(**kwargs)

            expiration_datetime = self.get_last_log_entry_datetime() + timedelta

            if now() > expiration_datetime:
                condition_context = {'workflow_instance': self}

                condition_result = escalation.evaluate_condition(
                    context=condition_context
                )
                if condition_result:
                    escalation_comment = escalation.get_comment()

                    self.do_transition(
                        comment=escalation_comment,
                        transition=escalation.transition
                    )

    def do_context_update(self, context):
        workflow_instance_context = self.loads()
        workflow_instance_context.update(context)
        self.dumps(context=workflow_instance_context)

    def do_transition(
        self, transition, comment=None, extra_data=None, user=None
    ):
        comment = comment or ''
        extra_data = extra_data or {}

        try:
            queryset_transitions = self.get_transition_choices(user=user).all()

            if queryset_transitions.filter(pk=transition.pk).exists():
                if extra_data:
                    self.do_context_update(context=extra_data)

                return transition.do_execute(
                    comment=comment, extra_data=json.dumps(obj=extra_data),
                    user=user, workflow_instance=self
                )
        except AttributeError:
            # No initial state has been set for this workflow.
            if settings.DEBUG:
                raise

    def dumps(self, context):
        """
        Serialize the context data.
        """
        self.context = json.dumps(obj=context)
        self.save()

    def get_context(self):
        # Keep the document instance in the workflow instance fresh when
        # there are cascade state actions, where a second state action is
        # triggered by the events generated by a first state action.
        self.document.refresh_from_db()
        context = {'workflow_instance': self}
        context['workflow_instance_context'] = self.loads()
        return context

    def get_current_state(self):
        """
        Actual State - The current state of the workflow. If there are
        multiple states available, for example: registered, approved,
        archived; this field will tell at the current state where the
        document is right now.
        """
        last_transition = self.get_last_transition()

        if last_transition:
            return last_transition.destination_state
        else:
            return self.workflow.get_initial_state()

    def get_last_log_entry(self):
        return self.log_entries.order_by('datetime').last()

    def get_last_log_entry_datetime(self):
        last_log_entry = self.get_last_log_entry()

        if last_log_entry:
            return last_log_entry.datetime
        else:
            return self.datetime

    def get_last_transition(self):
        """
        Last Transition - The last transition used by the last user to put
        the document in the actual state.
        """
        last_log_entry = self.get_last_log_entry()
        if last_log_entry:
            return last_log_entry.transition

    def get_runtime_context(self):
        """
        Alias of self.load() to get just the runtime context of the instance
        for ease of use in the condition template.
        """
        return self.loads()

    def get_transition_choices(self, user=None):
        WorkflowTransition = apps.get_model(
            app_label='document_states', model_name='WorkflowTransition'
        )

        current_state = self.get_current_state()

        if current_state:
            queryset = current_state.origin_transitions.all()

            if user:
                queryset = AccessControlList.objects.restrict_queryset(
                    permission=permission_workflow_instance_transition,
                    queryset=queryset, user=user
                )

            # Remove the transitions with a false return value.
            condition_context = {'workflow_instance': self}
            for entry in queryset:
                condition_result = entry.evaluate_condition(
                    context=condition_context
                )
                if not condition_result:
                    queryset = queryset.exclude(id=entry.pk)

            return queryset
        else:
            """
            This happens when a workflow has no initial state and a document
            whose document type has this workflow is created. We return an
            empty transition queryset.
            """
            return WorkflowTransition.objects.none()

    def loads(self):
        """
        Deserialize the context data.
        """
        return json.loads(s=self.context or '{}')


class WorkflowInstanceLogEntryBusinessLogicMixin:
    def get_extra_data(self):
        WorkflowTransitionField = apps.get_model(
            app_label='document_states', model_name='WorkflowTransitionField'
        )

        result = {}
        extra_data = self.loads()

        for key, value in extra_data.items():
            try:
                field = self.transition.fields.get(name=key)
            except WorkflowTransitionField.DoesNotExist:
                """
                There is a reference for a field that does not exist or
                has been deleted.
                """
            else:
                result[field.label] = value

        return result

    def loads(self):
        """
        Deserialize the context data.
        """
        return json.loads(s=self.extra_data or '{}')
