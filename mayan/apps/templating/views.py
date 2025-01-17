from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import TemplateSyntaxError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mayan.apps.documents.models.document_models import Document
from mayan.apps.views.generics import FormView
from mayan.apps.views.http import URL
from mayan.apps.views.view_mixins import ExternalObjectViewMixin

from .classes import Template
from .forms import DocumentTemplateSandboxForm
from .icons import icon_template_sandbox
from .permissions import permission_template_sandbox


class DocumentTemplateSandboxView(ExternalObjectViewMixin, FormView):
    external_object_class = Document
    external_object_permission = permission_template_sandbox
    external_object_pk_url_kwarg = 'document_id'
    form_class = DocumentTemplateSandboxForm
    view_icon = icon_template_sandbox

    def form_valid(self, form):
        path = reverse(
            kwargs={'document_id': self.external_object.pk},
            viewname='templating:document_template_sandbox'
        )
        url = URL(
            path=path, query={
                'template': form.cleaned_data['template']
            }
        )

        return HttpResponseRedirect(
            redirect_to=url.to_string()
        )

    def get_extra_context(self):
        return {
            'object': self.external_object,
            'title': _(
                message='Template sandbox for: %s'
            ) % self.external_object
        }

    def get_form_extra_kwargs(self):
        return {'model': Document, 'model_variable': 'document'}

    def get_initial(self):
        if settings.DEBUG:
            exception_list = (TemplateSyntaxError,)
        else:
            exception_list = (Exception, TemplateSyntaxError,)

        template_string = self.request.GET.get('template', '')
        try:
            template = Template(template_string=template_string)
            result = template.render(
                context={'document': self.external_object}
            )
        except exception_list as exception:
            result = ''
            error_message = _(
                message='Template error; %(exception)s'
            ) % {'exception': exception}

            result = error_message

        return {'result': result, 'template': template_string}
