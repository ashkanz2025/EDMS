from django.urls import re_path

from .views import (
    DocumentFileDriverListView, DocumentFileDriverAttributeListView,
    DocumentFileSubmitView, DocumentTypeFileMetadataSettingsEditView,
    DocumentTypeFileMetadataSubmitView
)

urlpatterns = [
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/drivers/$',
        name='document_file_metadata_driver_list',
        view=DocumentFileDriverListView.as_view()
    ),
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/submit/$',
        name='document_file_metadata_single_submit',
        view=DocumentFileSubmitView.as_view()
    ),
    re_path(
        route=r'^documents/files/multiple/submit/$',
        name='document_file_metadata_multiple_submit',
        view=DocumentFileSubmitView.as_view()
    ),
    re_path(
        route=r'^documents/files/drivers/(?P<document_file_driver_id>\d+)/attributes/$',
        name='document_file_metadata_driver_attribute_list',
        view=DocumentFileDriverAttributeListView.as_view()
    ),
    re_path(
        route=r'^document_types/(?P<document_type_id>\d+)/file_metadata/settings/$',
        name='document_type_file_metadata_settings',
        view=DocumentTypeFileMetadataSettingsEditView.as_view()
    ),
    re_path(
        route=r'^document_types/submit/$',
        name='document_type_file_metadata_submit',
        view=DocumentTypeFileMetadataSubmitView.as_view()
    )
]
