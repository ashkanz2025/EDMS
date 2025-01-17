from django.urls import re_path

from .api_views import (
    APIDocumentFileDetachedSignatureDetailView,
    APIDocumentFileDetachedSignatureListView,
    APIDocumentFileDetachedSignatureUploadView,
    APIDocumentFileEmbeddedSignatureDetailView,
    APIDocumentFileEmbeddedSignatureListView, APIDocumentFileSignDetachedView,
    APIDocumentFileSignEmbeddedView
)
from .views import (
    AllDocumentSignatureRefreshView, AllDocumentSignatureVerifyView,
    DocumentFileDetachedSignatureCreateView,
    DocumentFileEmbeddedSignatureCreateView,
    DocumentFileDetachedSignatureDeleteView, DocumentFileSignatureDetailView,
    DocumentFileDetachedSignatureDownloadView, DocumentFileSignatureListView,
    DocumentFileDetachedSignatureUploadView
)

urlpatterns_documents = [
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/signatures/$',
        name='document_file_signature_list',
        view=DocumentFileSignatureListView.as_view()
    ),
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/signatures/detached/create/$',
        name='document_file_signature_detached_create',
        view=DocumentFileDetachedSignatureCreateView.as_view()
    ),
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/signatures/detached/upload/$',
        name='document_file_signature_detached_upload',
        view=DocumentFileDetachedSignatureUploadView.as_view()
    ),
    re_path(
        route=r'^documents/files/(?P<document_file_id>\d+)/signatures/embedded/create/$',
        name='document_file_signature_embedded_create',
        view=DocumentFileEmbeddedSignatureCreateView.as_view()
    )
]

urlpatterns_signatures = [
    re_path(
        route=r'^signatures/detached/(?P<signature_id>\d+)/delete/$',
        name='document_file_signature_detached_delete',
        view=DocumentFileDetachedSignatureDeleteView.as_view()
    ),
    re_path(
        route=r'^signatures/detached/(?P<signature_id>\d+)/download/$',
        name='document_file_signature_detached_download',
        view=DocumentFileDetachedSignatureDownloadView.as_view()
    ),
    re_path(
        route=r'^signatures/(?P<signature_id>\d+)/details/$',
        name='document_file_signature_detail',
        view=DocumentFileSignatureDetailView.as_view()
    )
]

urlpatterns_tools = [
    re_path(
        route=r'^tools/all/document/file/signature/refresh/$',
        name='all_document_file_signature_refresh',
        view=AllDocumentSignatureRefreshView.as_view()
    ),
    re_path(
        route=r'^tools/all/document/file/signature/verify/$',
        name='all_document_file_signature_verify',
        view=AllDocumentSignatureVerifyView.as_view()
    )
]

urlpatterns = []
urlpatterns.extend(urlpatterns_documents)
urlpatterns.extend(urlpatterns_signatures)
urlpatterns.extend(urlpatterns_tools)

api_urls = [
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/detached/$',
        name='document-file-signature-detached-list',
        view=APIDocumentFileDetachedSignatureListView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/detached/sign/$',
        name='document-file-signature-detached-sign',
        view=APIDocumentFileSignDetachedView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/detached/upload/$',
        name='document-file-signature-detached-upload',
        view=APIDocumentFileDetachedSignatureUploadView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/detached/(?P<detached_signature_id>[0-9]+)/$',
        name='detachedsignature-detail',
        view=APIDocumentFileDetachedSignatureDetailView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/embedded/$',
        name='document-file-signature-embedded-list',
        view=APIDocumentFileEmbeddedSignatureListView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/embedded/sign/$',
        name='document-file-signature-embedded-sign',
        view=APIDocumentFileSignEmbeddedView.as_view()
    ),
    re_path(
        route=r'^documents/(?P<document_id>[0-9]+)/files/(?P<document_file_id>[0-9]+)/signatures/embedded/(?P<embedded_signature_id>[0-9]+)/$',
        name='embeddedsignature-detail',
        view=APIDocumentFileEmbeddedSignatureDetailView.as_view()
    )
]
