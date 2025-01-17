from rest_framework import status

from mayan.apps.django_gpg.permissions import permission_key_sign
from mayan.apps.django_gpg.tests.literals import TEST_KEY_PUBLIC_ID
from mayan.apps.django_gpg.tests.mixins import KeyTestMixin
from mayan.apps.documents.events import (
    event_document_file_created, event_document_file_edited,
    event_document_version_created, event_document_version_edited,
    event_document_version_page_created
)
from mayan.apps.documents.tests.mixins.document_mixins import (
    DocumentTestMixin
)
from mayan.apps.file_metadata.events import (
    event_file_metadata_document_file_finished,
    event_file_metadata_document_file_submitted
)
from mayan.apps.rest_api.tests.base import BaseAPITestCase

from ..events import event_embedded_signature_created
from ..permissions import (
    permission_document_file_sign_embedded,
    permission_document_file_signature_view
)

from .literals import TEST_SIGNED_DOCUMENT_PATH
from .mixins import EmbeddedSignatureAPIViewTestMixin


class EmbeddedSignatureDocumentAPIViewTestCase(
    DocumentTestMixin, EmbeddedSignatureAPIViewTestMixin,
    KeyTestMixin, BaseAPITestCase
):
    auto_upload_test_document = False

    def test_document_signature_embedded_detail_api_view_no_permission(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self._clear_events()

        response = self._request_test_document_signature_embedded_detail_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_detail_api_view_with_access(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self._clear_events()

        response = self._request_test_document_signature_embedded_detail_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.data['key_id'], TEST_KEY_PUBLIC_ID
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_signature_embedded_detail_api_view_with_access(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_signature_embedded_detail_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_list_api_view_no_permission(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self._clear_events()

        response = self._request_test_document_signature_embedded_list_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_list_api_view_with_access(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self._clear_events()

        response = self._request_test_document_signature_embedded_list_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'][0]['key_id'], TEST_KEY_PUBLIC_ID
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_signature_embedded_list_api_view_with_access(self):
        self._test_document_path = TEST_SIGNED_DOCUMENT_PATH
        self._upload_test_document()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_signature_view
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_signature_embedded_list_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_sign_api_view_with_no_permission(self):
        self._upload_test_document()
        self._create_test_key_private()

        signatures = self._test_document.file_latest.signatures.count()

        self._clear_events()

        response = self._request_test_document_signature_embedded_sign_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self._test_document.refresh_from_db()

        self.assertEqual(
            self._test_document.file_latest.signatures.count(),
            signatures
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_sign_api_view_with_document_access(self):
        self._upload_test_document()
        self._create_test_key_private()

        signatures = self._test_document.file_latest.signatures.count()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_sign_embedded
        )

        self._clear_events()

        response = self._request_test_document_signature_embedded_sign_view()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self._test_document.refresh_from_db()

        self.assertEqual(
            self._test_document.file_latest.signatures.count(),
            signatures
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_sign_api_view_with_key_access(self):
        self._upload_test_document()
        self._create_test_key_private()

        signatures = self._test_document.file_latest.signatures.count()

        self.grant_access(
            obj=self._test_key_private,
            permission=permission_key_sign
        )

        self._clear_events()

        response = self._request_test_document_signature_embedded_sign_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self._test_document.refresh_from_db()

        self.assertEqual(
            self._test_document.file_latest.signatures.count(),
            signatures
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_signature_embedded_sign_api_view_with_full_access(self):
        self._upload_test_document()
        self._create_test_key_private()

        signatures = self._test_document.file_latest.signatures.count()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_sign_embedded
        )
        self.grant_access(
            obj=self._test_key_private,
            permission=permission_key_sign
        )

        self._clear_events()

        response = self._request_test_document_signature_embedded_sign_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self._test_document.refresh_from_db()

        self.assertEqual(
            self._test_document.file_latest.signatures.count(),
            signatures + 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 8)

        test_document_file = self._test_document.file_latest
        test_document_version = self._test_document.versions.last()

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, self._test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, self._test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, self._test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, self._test_document)
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_document_version)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_document_version)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(
            events[5].target, test_document_version.pages.first()
        )
        self.assertEqual(
            events[5].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[6].action_object, self._test_document)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version)
        self.assertEqual(events[6].verb, event_document_version_edited.id)

        self.assertEqual(
            events[7].action_object,
            self._test_document.file_latest.signatures.first().embeddedsignature
        )
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, self._test_document_file)
        self.assertEqual(events[7].verb, event_embedded_signature_created.id)

    def test_trashed_document_signature_embedded_sign_api_view_with_full_access(self):
        self._upload_test_document()
        self._create_test_key_private()

        signatures = self._test_document.file_latest.signatures.count()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_sign_embedded
        )
        self.grant_access(
            obj=self._test_key_private,
            permission=permission_key_sign
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_signature_embedded_sign_view()
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self._test_document.refresh_from_db()

        self.assertEqual(
            self._test_document.file_latest.signatures.count(),
            signatures
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)
