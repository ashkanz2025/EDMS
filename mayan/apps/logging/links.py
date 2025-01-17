from django.utils.translation import gettext_lazy as _

from mayan.apps.navigation.links import Link
from mayan.apps.navigation.utils import get_content_type_kwargs_factory

from .icons import (
    icon_global_error_log_entry_list, icon_object_error_log_entry_delete,
    icon_object_error_log_entry_list, icon_object_error_log_entry_list_clear
)
from .permissions import (
    permission_error_log_entry_delete, permission_error_log_entry_view
)

link_global_error_log_partition_entry_list = Link(
    icon=icon_global_error_log_entry_list, text=_(message='Global error log'),
    view='logging:global_error_log_partition_entry_list'
)
link_object_error_log_entry_delete = Link(
    icon=icon_object_error_log_entry_delete,
    kwargs={
        'app_label': 'resolved_object.error_log_partition.content_type.app_label',
        'model_name': 'resolved_object.error_log_partition.content_type.model',
        'object_id': 'resolved_object.error_log_partition.object_id',
        'error_log_partition_entry_id': 'resolved_object.pk'
    }, permission=permission_error_log_entry_delete, tags='dangerous',
    text=_(message='Delete'), view='logging:object_error_log_entry_delete'
)
link_object_error_log_entry_list = Link(
    icon=icon_object_error_log_entry_list,
    kwargs=get_content_type_kwargs_factory(variable_name='resolved_object'),
    permission=permission_error_log_entry_view, text=_(message='Errors'),
    view='logging:object_error_log_entry_list'
)
link_object_error_log_entry_list_clear = Link(
    icon=icon_object_error_log_entry_list_clear,
    kwargs=get_content_type_kwargs_factory(variable_name='resolved_object'),
    permission=permission_error_log_entry_delete, text=_(message='Clear errors'),
    view='logging:object_error_log_entry_list_clear'
)
