from mayan.apps.documents.document_file_actions import (
    DocumentFileActionAppendNewPages, DocumentFileActionNothing,
    DocumentFileActionUseNewPages
)
from mayan.apps.documents.events import (
    event_document_created, event_document_file_created,
    event_document_file_edited, event_document_version_created,
    event_document_version_edited, event_document_version_page_created
)
from mayan.apps.documents.models.document_models import Document
from mayan.apps.documents.permissions import (
    permission_document_create, permission_document_file_new
)
from mayan.apps.documents.tests.base import GenericDocumentViewTestCase
from mayan.apps.documents.tests.literals import (
    TEST_DOCUMENT_SMALL_CHECKSUM, TEST_FILE_COMPRESSED_PATH
)
from mayan.apps.file_metadata.events import (
    event_file_metadata_document_file_finished,
    event_file_metadata_document_file_submitted
)
from mayan.apps.source_compressed.source_backends.literals import (
    SOURCE_UNCOMPRESS_CHOICE_ALWAYS, SOURCE_UNCOMPRESS_CHOICE_ASK,
    SOURCE_UNCOMPRESS_CHOICE_NEVER
)
from mayan.apps.sources.events import event_source_created
from mayan.apps.sources.models import Source
from mayan.apps.sources.permissions import permission_sources_create
from mayan.apps.sources.tests.mixins.source_view_mixins import (
    SourceActionViewTestMixin, SourceViewTestMixin
)

from .mixins import WebFormSourceTestMixin


class WebFormSourceBackendActionDocumentFileUploadViewTestCase(
    WebFormSourceTestMixin, SourceActionViewTestMixin,
    GenericDocumentViewTestCase
):
    _test_source_create_auto = False
    auto_upload_test_document = True

    def test_basic_no_permission(self):
        self._test_source_create()

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_document_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_source_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_full_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count + 1
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count + 1
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )
        self.assertEqual(
            self._test_document.versions.all()[1].pages.count(), 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 7)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page = test_document_version.pages.first()

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_document_version)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_document_version)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version_page)
        self.assertEqual(
            events[5].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[6].action_object, test_document)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version)
        self.assertEqual(events[6].verb, event_document_version_edited.id)

    def test_basic_with_full_access_trashed_document(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_comment(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view(
            extra_data={'document-comment': 'test-comment'}
        )
        self.assertEqual(response.status_code, 302)

        self._test_document.refresh_from_db()

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count + 1
        )
        self.assertEqual(
            self._test_document.file_latest.comment, 'test-comment'
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count + 1
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )
        self.assertEqual(
            self._test_document.versions.all()[1].pages.count(), 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 7)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page = test_document_version.pages.first()

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_document_version)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_document_version)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version_page)
        self.assertEqual(
            events[5].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[6].action_object, test_document)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version)
        self.assertEqual(events[6].verb, event_document_version_edited.id)

    def test_document_file_action_append(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view(
            extra_data={
                'document-action_name': DocumentFileActionAppendNewPages.action_id
            }
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count + 1
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count + 1
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )
        self.assertEqual(
            self._test_document.versions.all()[1].pages.count(),
            self._test_document.files.all()[0].pages.count() + self._test_document.files.all()[1].pages.count()
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 8)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page_first = test_document_version.pages.all()[0]
        test_document_version_page_last = test_document_version.pages.all()[1]

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_document_version)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_document_version)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version_page_first)
        self.assertEqual(
            events[5].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[6].action_object, test_document_version)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version_page_last)
        self.assertEqual(
            events[6].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[7].action_object, test_document)
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, test_document_version)
        self.assertEqual(events[7].verb, event_document_version_edited.id)

    def test_document_file_action_keep(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view(
            extra_data={
                'document-action_name': DocumentFileActionNothing.action_id
            }
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count + 1
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 4)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

    def test_document_file_action_new(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_new
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_file_new
        )

        test_document_count = Document.objects.count()
        test_document_file_count = self._test_document.files.count()
        test_document_version_count = self._test_document.versions.count()
        test_document_version_page_count = self._test_document.versions.all()[0].pages.count()

        self._clear_events()

        response = self._request_test_source_document_file_upload_view(
            extra_data={
                'document-action_name': DocumentFileActionUseNewPages.action_id
            }
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), test_document_count
        )
        self.assertEqual(
            self._test_document.files.count(), test_document_file_count + 1
        )
        self.assertEqual(
            self._test_document.versions.count(),
            test_document_version_count + 1
        )
        self.assertEqual(
            self._test_document.versions.all()[0].pages.count(),
            test_document_version_page_count
        )
        self.assertEqual(
            self._test_document.versions.all()[1].pages.count(), 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 7)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page = test_document_version.pages.first()

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document_file)
        self.assertEqual(events[0].verb, event_document_file_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_edited.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, test_document_file)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_document_version)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_document_version)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version_page)
        self.assertEqual(
            events[5].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[6].action_object, test_document)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version)
        self.assertEqual(events[6].verb, event_document_version_edited.id)


class WebFormSourceBackendActionDocumentUploadViewTestCase(
    WebFormSourceTestMixin, SourceActionViewTestMixin,
    GenericDocumentViewTestCase
):
    _test_source_create_auto = False
    auto_upload_test_document = False

    def test_basic_with_no_permission(self):
        self._test_source_create()

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            Document.objects.count(), document_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_document_type_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_source_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            Document.objects.count(), document_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_basic_with_full_access(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 1
        )
        self.assertEqual(
            Document.objects.first().file_latest.checksum,
            TEST_DOCUMENT_SMALL_CHECKSUM
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 8)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page = test_document_version.pages.first()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document)
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, self._test_case_user)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(events[2].verb, event_document_file_edited.id)

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, test_document_file)
        self.assertEqual(events[4].target, test_document_file)
        self.assertEqual(
            events[4].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[5].action_object, test_document)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version)
        self.assertEqual(events[5].verb, event_document_version_created.id)

        self.assertEqual(events[6].action_object, test_document_version)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version_page)
        self.assertEqual(
            events[6].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[7].action_object, test_document)
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, test_document_version)
        self.assertEqual(events[7].verb, event_document_version_edited.id)

    def test_compressed_always(self):
        self._test_source_create(
            extra_data={'uncompress': SOURCE_UNCOMPRESS_CHOICE_ALWAYS}
        )

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view(
            test_file_path=TEST_FILE_COMPRESSED_PATH
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 2
        )

        self.assertTrue(
            'first document.pdf' in Document.objects.values_list(
                'label', flat=True
            )
        )
        self.assertTrue(
            'second document.pdf' in Document.objects.values_list(
                'label', flat=True
            )
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 17)

        test_documents = Document.objects.all()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_documents[0])
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_documents[0])
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_documents[0].file_latest)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_documents[0])
        self.assertEqual(events[2].actor, self._test_case_user)
        self.assertEqual(events[2].target, test_documents[0].file_latest)
        self.assertEqual(events[2].verb, event_document_file_edited.id)

        self.assertEqual(events[3].action_object, test_documents[0])
        self.assertEqual(events[3].actor, test_documents[0].file_latest)
        self.assertEqual(events[3].target, test_documents[0].file_latest)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[4].action_object, test_documents[0])
        self.assertEqual(events[4].actor, test_documents[0].file_latest)
        self.assertEqual(events[4].target, test_documents[0].file_latest)
        self.assertEqual(
            events[4].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[5].action_object, test_documents[0])
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_documents[0].version_active)
        self.assertEqual(events[5].verb, event_document_version_created.id)

        self.assertEqual(
            events[6].action_object, test_documents[0].version_active
        )
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(
            events[6].target, test_documents[0].version_active.pages.first()
        )
        self.assertEqual(
            events[6].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[7].action_object, test_documents[0])
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, test_documents[0].version_active)
        self.assertEqual(events[7].verb, event_document_version_edited.id)

        self.assertEqual(events[8].action_object, self._test_document_type)
        self.assertEqual(events[8].actor, self._test_case_user)
        self.assertEqual(events[8].target, test_documents[1])
        self.assertEqual(events[8].verb, event_document_created.id)

        self.assertEqual(events[9].action_object, test_documents[1])
        self.assertEqual(events[9].actor, self._test_case_user)
        self.assertEqual(events[9].target, test_documents[1].file_latest)
        self.assertEqual(events[9].verb, event_document_file_created.id)

        self.assertEqual(events[10].action_object, test_documents[1])
        self.assertEqual(events[10].actor, self._test_case_user)
        self.assertEqual(events[10].target, test_documents[1].file_latest)
        self.assertEqual(events[10].verb, event_document_file_edited.id)

        self.assertEqual(events[11].action_object, test_documents[1])
        self.assertEqual(events[11].actor, test_documents[1].file_latest)
        self.assertEqual(events[11].target, test_documents[1].file_latest)
        self.assertEqual(
            events[11].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[12].action_object, test_documents[1])
        self.assertEqual(events[12].actor, test_documents[1].file_latest)
        self.assertEqual(events[12].target, test_documents[1].file_latest)
        self.assertEqual(
            events[12].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[13].action_object, test_documents[1])
        self.assertEqual(events[13].actor, self._test_case_user)
        self.assertEqual(events[13].target, test_documents[1].version_active)
        self.assertEqual(events[13].verb, event_document_version_created.id)

        self.assertEqual(
            events[14].action_object, test_documents[1].version_active
        )
        self.assertEqual(events[14].actor, self._test_case_user)
        self.assertEqual(
            events[14].target, test_documents[1].version_active.pages.first()
        )
        self.assertEqual(
            events[14].verb, event_document_version_page_created.id
        )

        self.assertEqual(
            events[15].action_object, test_documents[1].version_active
        )
        self.assertEqual(events[15].actor, self._test_case_user)
        self.assertEqual(
            events[15].target, test_documents[1].version_active.pages.last()
        )
        self.assertEqual(
            events[15].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[16].action_object, test_documents[1])
        self.assertEqual(events[16].actor, self._test_case_user)
        self.assertEqual(events[16].target, test_documents[1].version_active)
        self.assertEqual(events[16].verb, event_document_version_edited.id)

    def test_compressed_ask_false(self):
        self._silence_logger(name='mayan.apps.converter.backends')

        self._test_source_create(
            extra_data={'uncompress': SOURCE_UNCOMPRESS_CHOICE_ASK}
        )

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view(
            extra_data={'source-expand': False},
            test_file_path=TEST_FILE_COMPRESSED_PATH
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 6)

        test_documents = Document.objects.all()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_documents[0])
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_documents[0])
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_documents[0].file_latest)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_documents[0])
        self.assertEqual(events[2].actor, test_documents[0].file_latest)
        self.assertEqual(events[2].target, test_documents[0].file_latest)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_documents[0])
        self.assertEqual(events[3].actor, test_documents[0].file_latest)
        self.assertEqual(events[3].target, test_documents[0].file_latest)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_documents[0])
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_documents[0].version_active)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_documents[0])
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_documents[0].version_active)
        self.assertEqual(events[5].verb, event_document_version_edited.id)

    def test_compressed_ask_true(self):
        self._test_source_create(
            extra_data={'uncompress': SOURCE_UNCOMPRESS_CHOICE_ASK}
        )

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view(
            extra_data={'source-expand': True},
            test_file_path=TEST_FILE_COMPRESSED_PATH
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 2
        )

        self.assertTrue(
            'first document.pdf' in Document.objects.values_list(
                'label', flat=True
            )
        )
        self.assertTrue(
            'second document.pdf' in Document.objects.values_list(
                'label', flat=True
            )
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 17)

        test_documents = Document.objects.all()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_documents[0])
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_documents[0])
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_documents[0].file_latest)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_documents[0])
        self.assertEqual(events[2].actor, self._test_case_user)
        self.assertEqual(events[2].target, test_documents[0].file_latest)
        self.assertEqual(events[2].verb, event_document_file_edited.id)

        self.assertEqual(events[3].action_object, test_documents[0])
        self.assertEqual(events[3].actor, test_documents[0].file_latest)
        self.assertEqual(events[3].target, test_documents[0].file_latest)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[4].action_object, test_documents[0])
        self.assertEqual(events[4].actor, test_documents[0].file_latest)
        self.assertEqual(events[4].target, test_documents[0].file_latest)
        self.assertEqual(
            events[4].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[5].action_object, test_documents[0])
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_documents[0].version_active)
        self.assertEqual(events[5].verb, event_document_version_created.id)

        self.assertEqual(
            events[6].action_object, test_documents[0].version_active
        )
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(
            events[6].target, test_documents[0].version_active.pages.first()
        )
        self.assertEqual(
            events[6].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[7].action_object, test_documents[0])
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, test_documents[0].version_active)
        self.assertEqual(events[7].verb, event_document_version_edited.id)

        self.assertEqual(events[8].action_object, self._test_document_type)
        self.assertEqual(events[8].actor, self._test_case_user)
        self.assertEqual(events[8].target, test_documents[1])
        self.assertEqual(events[8].verb, event_document_created.id)

        self.assertEqual(events[9].action_object, test_documents[1])
        self.assertEqual(events[9].actor, self._test_case_user)
        self.assertEqual(events[9].target, test_documents[1].file_latest)
        self.assertEqual(events[9].verb, event_document_file_created.id)

        self.assertEqual(events[10].action_object, test_documents[1])
        self.assertEqual(events[10].actor, self._test_case_user)
        self.assertEqual(events[10].target, test_documents[1].file_latest)
        self.assertEqual(events[10].verb, event_document_file_edited.id)

        self.assertEqual(events[11].action_object, test_documents[1])
        self.assertEqual(events[11].actor, test_documents[1].file_latest)
        self.assertEqual(events[11].target, test_documents[1].file_latest)
        self.assertEqual(
            events[11].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[12].action_object, test_documents[1])
        self.assertEqual(events[12].actor, test_documents[1].file_latest)
        self.assertEqual(events[12].target, test_documents[1].file_latest)
        self.assertEqual(
            events[12].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[13].action_object, test_documents[1])
        self.assertEqual(events[13].actor, self._test_case_user)
        self.assertEqual(events[13].target, test_documents[1].version_active)
        self.assertEqual(events[13].verb, event_document_version_created.id)

        self.assertEqual(
            events[14].action_object, test_documents[1].version_active
        )
        self.assertEqual(events[14].actor, self._test_case_user)
        self.assertEqual(
            events[14].target, test_documents[1].version_active.pages.first()
        )
        self.assertEqual(
            events[14].verb, event_document_version_page_created.id
        )

        self.assertEqual(
            events[15].action_object, test_documents[1].version_active
        )
        self.assertEqual(events[15].actor, self._test_case_user)
        self.assertEqual(
            events[15].target, test_documents[1].version_active.pages.last()
        )
        self.assertEqual(
            events[15].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[16].action_object, test_documents[1])
        self.assertEqual(events[16].actor, self._test_case_user)
        self.assertEqual(events[16].target, test_documents[1].version_active)
        self.assertEqual(events[16].verb, event_document_version_edited.id)

    def test_compressed_never(self):
        self._silence_logger(name='mayan.apps.converter.backends')

        self._test_source_create(
            extra_data={'uncompress': SOURCE_UNCOMPRESS_CHOICE_NEVER}
        )

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view(
            test_file_path=TEST_FILE_COMPRESSED_PATH
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 6)

        test_documents = Document.objects.all()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_documents[0])
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_documents[0])
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_documents[0].file_latest)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_documents[0])
        self.assertEqual(events[2].actor, test_documents[0].file_latest)
        self.assertEqual(events[2].target, test_documents[0].file_latest)
        self.assertEqual(
            events[2].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[3].action_object, test_documents[0])
        self.assertEqual(events[3].actor, test_documents[0].file_latest)
        self.assertEqual(events[3].target, test_documents[0].file_latest)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[4].action_object, test_documents[0])
        self.assertEqual(events[4].actor, self._test_case_user)
        self.assertEqual(events[4].target, test_documents[0].version_active)
        self.assertEqual(events[4].verb, event_document_version_created.id)

        self.assertEqual(events[5].action_object, test_documents[0])
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_documents[0].version_active)
        self.assertEqual(events[5].verb, event_document_version_edited.id)

    def test_language(self):
        self._test_source_create()

        self.grant_access(
            obj=self._test_document_type,
            permission=permission_document_create
        )
        self.grant_access(
            obj=self._test_source, permission=permission_document_create
        )

        document_count = Document.objects.count()

        self._clear_events()

        response = self._request_test_source_document_upload_post_view(
            extra_data={'document-language': 'deu'}
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Document.objects.count(), document_count + 1
        )
        self.assertEqual(
            Document.objects.first().file_latest.checksum,
            TEST_DOCUMENT_SMALL_CHECKSUM
        )
        self.assertEqual(Document.objects.first().language, 'deu')

        events = self._get_test_events()
        self.assertEqual(events.count(), 8)

        test_document = Document.objects.first()
        test_document_file = test_document.file_latest
        test_document_version = test_document.version_active
        test_document_version_page = test_document_version.pages.first()

        self.assertEqual(events[0].action_object, self._test_document_type)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, test_document)
        self.assertEqual(events[0].verb, event_document_created.id)

        self.assertEqual(events[1].action_object, test_document)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, test_document_file)
        self.assertEqual(events[1].verb, event_document_file_created.id)

        self.assertEqual(events[2].action_object, test_document)
        self.assertEqual(events[2].actor, self._test_case_user)
        self.assertEqual(events[2].target, test_document_file)
        self.assertEqual(events[2].verb, event_document_file_edited.id)

        self.assertEqual(events[3].action_object, test_document)
        self.assertEqual(events[3].actor, test_document_file)
        self.assertEqual(events[3].target, test_document_file)
        self.assertEqual(
            events[3].verb, event_file_metadata_document_file_submitted.id
        )

        self.assertEqual(events[4].action_object, test_document)
        self.assertEqual(events[4].actor, test_document_file)
        self.assertEqual(events[4].target, test_document_file)
        self.assertEqual(
            events[4].verb, event_file_metadata_document_file_finished.id
        )

        self.assertEqual(events[5].action_object, test_document)
        self.assertEqual(events[5].actor, self._test_case_user)
        self.assertEqual(events[5].target, test_document_version)
        self.assertEqual(events[5].verb, event_document_version_created.id)

        self.assertEqual(events[6].action_object, test_document_version)
        self.assertEqual(events[6].actor, self._test_case_user)
        self.assertEqual(events[6].target, test_document_version_page)
        self.assertEqual(
            events[6].verb, event_document_version_page_created.id
        )

        self.assertEqual(events[7].action_object, test_document)
        self.assertEqual(events[7].actor, self._test_case_user)
        self.assertEqual(events[7].target, test_document_version)
        self.assertEqual(events[7].verb, event_document_version_edited.id)


class WebFormSourceBackendViewTestCase(
    WebFormSourceTestMixin, SourceViewTestMixin, GenericDocumentViewTestCase
):
    _test_source_create_auto = False
    auto_upload_test_document = False

    def test_web_form_source_create_get_view_no_permission(self):
        source_count = Source.objects.count()

        self._clear_events()

        response = self._request_test_source_create_get_view()
        self.assertEqual(response.status_code, 403)

        self.assertEqual(Source.objects.count(), source_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_web_form_source_create_get_view_with_permission(self):
        self.grant_permission(permission=permission_sources_create)

        source_count = Source.objects.count()

        self._clear_events()

        response = self._request_test_source_create_get_view()
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Source.objects.count(), source_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_web_form_source_create_post_view_no_permission(self):
        source_count = Source.objects.count()

        self._clear_events()

        response = self._request_test_source_create_post_view()
        self.assertEqual(response.status_code, 403)

        self.assertEqual(Source.objects.count(), source_count)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_web_form_source_create_post_view_with_permission(self):
        self.grant_permission(permission=permission_sources_create)

        source_count = Source.objects.count()

        self._clear_events()

        response = self._request_test_source_create_post_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Source.objects.count(), source_count + 1)

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, None)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self._test_source)
        self.assertEqual(events[0].verb, event_source_created.id)
