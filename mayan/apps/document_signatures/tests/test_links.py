from django.urls import reverse

from mayan.apps.documents.tests.base import GenericDocumentViewTestCase
from mayan.apps.documents.tests.literals import TEST_FILE_SMALL_PATH

from ..links import (
    link_document_file_signature_detached_delete,
    link_document_file_signature_detail
)
from ..permissions import (
    permission_document_file_signature_delete,
    permission_document_file_signature_view
)
from .literals import TEST_SIGNED_DOCUMENT_PATH
from .mixins import DetachedSignatureTestMixin


class DocumentSignatureLinksTestCase(
    DetachedSignatureTestMixin, GenericDocumentViewTestCase
):
    def test_document_file_signature_detail_link_no_permission(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.add_test_view(
            test_object=self._test_document.file_latest.signatures.first()
        )
        context = self.get_test_view()
        resolved_link = link_document_file_signature_detail.resolve(
            context=context
        )

        self.assertEqual(resolved_link, None)

    def test_document_file_signature_detail_link_with_permission(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self.add_test_view(
            test_object=self._test_document.file_latest.signatures.first()
        )
        context = self.get_test_view()
        resolved_link = link_document_file_signature_detail.resolve(
            context=context
        )

        self.assertNotEqual(resolved_link, None)
        self.assertEqual(
            resolved_link.url,
            reverse(
                viewname=link_document_file_signature_detail.view,
                kwargs={
                    'signature_id': self._test_document.file_latest.signatures.first().pk,
                }
            )
        )

    def test_document_file_signature_detached_delete_link_no_permission(self):
        self._test_document_path = TEST_FILE_SMALL_PATH
        self._upload_test_document()

        self._upload_test_detached_signature()

        self.add_test_view(
            test_object=self._test_document.file_latest.signatures.first()
        )
        context = self.get_test_view()
        resolved_link = link_document_file_signature_detached_delete.resolve(
            context=context
        )
        self.assertEqual(resolved_link, None)

    def test_document_file_signature_detached_delete_link_with_permission(self):
        self._test_document_path = TEST_FILE_SMALL_PATH
        self._upload_test_document()

        self._upload_test_detached_signature()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_delete
        )

        self.add_test_view(
            test_object=self._test_document.file_latest.signatures.first()
        )
        context = self.get_test_view()
        resolved_link = link_document_file_signature_detached_delete.resolve(
            context=context
        )
        self.assertNotEqual(resolved_link, None)
        self.assertEqual(
            resolved_link.url,
            reverse(
                viewname=link_document_file_signature_detached_delete.view,
                kwargs={
                    'signature_id': self._test_document.file_latest.signatures.first().pk,
                }
            )
        )



from mayan.apps.django_gpg.tests.mixins import KeyTestMixin
from mayan.apps.documents.tests.base import GenericDocumentViewTestCase
from mayan.apps.documents.tests.literals import TEST_FILE_SMALL_PATH

from ..permissions import permission_document_file_signature_view

from .mixins import DetachedSignatureTestMixin, SignatureViewTestMixin

class DocumentSignatureViewLinksTestCase(
    KeyTestMixin, DetachedSignatureTestMixin, SignatureViewTestMixin,
    GenericDocumentViewTestCase
):
    """
    Test the delete view in the list view context which has two main objects:
    the document file and the signature.
    """

    auto_upload_test_document = False

    def test_document_file_signature_detached_delete_link_in_view_with_full_permission(self):
        self._test_document_path = TEST_FILE_SMALL_PATH
        self._upload_test_document()

        self._upload_test_detached_signature()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_delete
        )
        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self._clear_events()

        response = self._request_test_document_file_signature_list_view(
            document=self._test_document
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].count(), 1)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)
