from django.apps import apps
from django.db.models.signals import post_delete
from django.utils.translation import gettext_lazy as _

from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.menus import menu_list_facet, menu_tools
from mayan.apps.documents.menus import menu_documents
from mayan.apps.documents.permissions import permission_document_view
from mayan.apps.documents.signals import signal_post_document_file_upload
from mayan.apps.navigation.source_columns import SourceColumn

from .classes import DuplicateBackend
from .handlers import (
    handler_remove_empty_duplicates_lists, handler_scan_duplicates_for
)
from .links import (
    link_document_duplicates_list, link_duplicated_document_list,
    link_duplicated_document_scan
)


class DuplicatesApp(MayanAppConfig):
    app_namespace = 'duplicates'
    app_url = 'duplicates'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.duplicates'
    verbose_name = _(message='Duplicates')

    def ready(self):
        super().ready()

        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )

        DuplicateBackendEntry = self.get_model(
            model_name='DuplicateBackendEntry'
        )
        DuplicateSourceDocument = self.get_model(
            model_name='DuplicateSourceDocument'
        )
        DuplicateTargetDocument = self.get_model(
            model_name='DuplicateTargetDocument'
        )

        DuplicateBackend.load_modules()

        SourceColumn(
            func=lambda context: DuplicateBackendEntry.objects.get_duplicates_of(
                document=context['object'],
                permission=permission_document_view,
                user=context['request'].user
            ).count(), include_label=True, label=_(message='Duplicates'),
            order=99, source=DuplicateSourceDocument
        )

        SourceColumn(
            attribute='backend', include_label=True,
            label=_(message='Duplicate backend'), order=99,
            source=DuplicateTargetDocument
        )

        menu_documents.bind_links(
            links=(link_duplicated_document_list,)
        )
        menu_list_facet.bind_links(
            links=(link_document_duplicates_list,),
            sources=(Document,)
        )
        menu_tools.bind_links(
            links=(link_duplicated_document_scan,)
        )

        post_delete.connect(
            dispatch_uid='duplicates_handler_remove_empty_duplicates_lists',
            receiver=handler_remove_empty_duplicates_lists,
            sender=Document
        )
        signal_post_document_file_upload.connect(
            dispatch_uid='duplicates_handler_scan_duplicates_for',
            receiver=handler_scan_duplicates_for
        )
