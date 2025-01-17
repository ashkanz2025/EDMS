from django.contrib.contenttypes.models import ContentType

from rest_framework import status

from mayan.apps.documents.tests.mixins.document_mixins import (
    DocumentTestMixin
)
from mayan.apps.rest_api.tests.base import BaseAPITestCase

from ..permissions import permission_events_view

from .mixins.event_mixins import (
    EventListAPIViewTestMixin, ObjectEventAPITestMixin
)
from .mixins.event_type_mixins import EventTypeNamespaceAPITestMixin


class EventListAPIViewTestCase(
    DocumentTestMixin, EventListAPIViewTestMixin, BaseAPITestCase
):
    def test_event_list_api_view_no_permission(self):
        response = self._request_test_event_list_api_view()
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_event_list_api_view_with_access(self):
        self.grant_permission(permission=permission_events_view)

        response = self._request_test_event_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventTypeNamespaceAPITestCase(
    EventTypeNamespaceAPITestMixin, BaseAPITestCase
):
    def setUp(self):
        super().setUp()
        self._create_test_event_type()

    def test_event_type_list_api_view(self):
        response = self._request_test_event_type_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_type_namespace_list_api_view(self):
        response = self._request_test_event_namespace_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_type_namespace_event_type_list_api_view(self):
        response = self._request_test_event_type_namespace_event_type_list_api_view()

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ObjectEventAPITestCase(
    DocumentTestMixin, ObjectEventAPITestMixin, BaseAPITestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self._test_object = self._test_document_type

        content_type = ContentType.objects.get_for_model(
            model=self._test_object
        )

        self.view_arguments = {
            'app_label': content_type.app_label,
            'model_name': content_type.model,
            'object_id': self._test_object.pk
        }

    def test_object_event_list_api_view_no_permission(self):
        response = self._request_object_event_list_api_view()
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND
        )

    def test_object_event_list_api_view_with_access(self):
        self.grant_access(
            obj=self._test_object, permission=permission_events_view
        )
        response = self._request_object_event_list_api_view()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
