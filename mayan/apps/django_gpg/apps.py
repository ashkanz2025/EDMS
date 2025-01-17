from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import (
    permission_acl_edit, permission_acl_view
)
from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.menus import (
    menu_list_facet, menu_object, menu_related, menu_secondary, menu_setup
)
from mayan.apps.events.classes import EventModelRegistry, ModelEventType
from mayan.apps.navigation.source_columns import SourceColumn

from .classes import KeyStub
from .events import event_key_downloaded
from .links import (
    link_key_delete, link_key_detail, link_key_download, link_key_query,
    link_key_receive, link_key_setup, link_key_upload, link_private_key_list,
    link_public_key_list
)
from .permissions import (
    permission_key_delete, permission_key_download, permission_key_sign,
    permission_key_view
)


class DjangoGPGApp(MayanAppConfig):
    app_namespace = 'django_gpg'
    app_url = 'keys'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.django_gpg'
    verbose_name = _(message='Django GPG')

    def ready(self):
        super().ready()

        Key = self.get_model(model_name='Key')

        EventModelRegistry.register(model=Key)
        ModelEventType.register(
            model=Key, event_types=(
                event_key_downloaded,
            )
        )
        ModelPermission.register(
            model=Key, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_key_delete, permission_key_download,
                permission_key_sign, permission_key_view
            )
        )

        SourceColumn(
            attribute='key_id', is_identifier=True, label=_(message='Key ID'),
            source=Key
        )
        SourceColumn(attribute='user_id', include_label=True, source=Key)

        SourceColumn(
            attribute='key_id', include_label=True, label=_(message='Key ID'),
            source=KeyStub
        )
        SourceColumn(
            attribute='key_type', include_label=True, label=_(message='Type'),
            source=KeyStub
        )
        SourceColumn(
            attribute='date', include_label=True, label=_(message='Creation date'),
            source=KeyStub
        )
        SourceColumn(
            func=lambda context: context['object'].expires or _(
                message='No expiration'
            ), include_label=True, label=_(message='Expiration date'),
            source=KeyStub
        )
        SourceColumn(
            attribute='length', include_label=True, label=_(message='Length'),
            source=KeyStub
        )
        SourceColumn(
            func=lambda context: ', '.join(context['object'].user_id),
            include_label=True, label=_(message='User ID'), source=KeyStub
        )

        menu_list_facet.bind_links(
            links=(link_key_detail,), sources=(Key,)
        )
        menu_object.bind_links(
            links=(link_key_receive,), sources=(KeyStub,)
        )

        menu_object.bind_links(
            links=(link_key_delete, link_key_download),
            sources=(Key,)
        )
        menu_related.bind_links(
            links=(link_private_key_list, link_public_key_list),
            sources=(
                'django_gpg:key_public_list', 'django_gpg:key_private_list',
                'django_gpg:key_query', 'django_gpg:key_query_results',
                'django_gpg:key_upload', Key, KeyStub
            )
        )
        menu_secondary.bind_links(
            links=(link_key_query, link_key_upload),
            sources=(
                'django_gpg:key_public_list', 'django_gpg:key_private_list',
                'django_gpg:key_query', 'django_gpg:key_query_results',
                'django_gpg:key_upload', Key, KeyStub
            )
        )
        menu_setup.bind_links(
            links=(link_key_setup,)
        )
