from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import Tag

from acls.api import class_permissions
from common.utils import encapsulate
from documents.models import Document
from navigation.api import (register_links, register_top_menu,
    register_model_list_columns, register_multi_item_links)
from rest_api.classes import APIEndPoint

from .links import (tag_list, tag_create, tag_attach,
    tag_document_list, tag_delete, tag_edit, tag_tagged_item_list,
    tag_multiple_delete, tag_acl_list, tag_multiple_attach,
    single_document_multiple_tag_remove, multiple_documents_selection_tag_remove)
from .permissions import (PERMISSION_TAG_ATTACH, PERMISSION_TAG_REMOVE,
    PERMISSION_TAG_DELETE, PERMISSION_TAG_EDIT, PERMISSION_TAG_VIEW)
from .urls import api_urls
from .widgets import (get_tags_inline_widget_simple, single_tag_widget)

register_model_list_columns(Tag, [
    {
        'name': _(u'Preview'),
        'attribute': encapsulate(lambda x: single_tag_widget(x))
    },
    {
        'name': _(u'Tagged items'),
        'attribute': encapsulate(lambda x: x.taggit_taggeditem_items.count())
    }
])

register_model_list_columns(Document, [
    {
        'name': _(u'Tags'), 'attribute':
        encapsulate(lambda x: get_tags_inline_widget_simple(x))
    },
])

register_links(Tag, [tag_tagged_item_list, tag_edit, tag_delete, tag_acl_list])
register_multi_item_links(['tags:tag_list'], [tag_multiple_delete])
register_links([Tag, 'tags:tag_list', 'tags:tag_create'], [tag_list, tag_create], menu_name='secondary_menu')
register_top_menu('tags', link={'text': _(u'Tags'), 'view': 'tags:tag_list', 'famfam': 'tag_blue'}, children_view_regex=[r'^tag_(list|create|delete|edit|tagged|acl)'])

register_links(Document, [tag_document_list], menu_name='form_header')
register_links(['tags:document_tags', 'tags:tag_remove', 'tag_multiple_remove', 'tag_attach'], [tag_attach], menu_name='sidebar')
register_multi_item_links(['document_tags'], [single_document_multiple_tag_remove])

register_multi_item_links(['documents:document_find_duplicates', 'folders:folder_view', 'indexes:index_instance_node_view', 'documents:document_type_document_list', 'search:search', 'search:results', 'linking:document_group_view', 'documents:document_list', 'documents:document_list_recent', 'tags:tag_tagged_item_list'], [tag_multiple_attach, multiple_documents_selection_tag_remove])

class_permissions(Document, [
    PERMISSION_TAG_ATTACH, PERMISSION_TAG_REMOVE,
])

class_permissions(Tag, [
    PERMISSION_TAG_DELETE, PERMISSION_TAG_EDIT, PERMISSION_TAG_VIEW,
])

def tag_documents(self):
    return Document.objects.filter(tags__in=[self])

Document.add_to_class('tags', TaggableManager())
Tag.add_to_class('documents', property(tag_documents))

endpoint = APIEndPoint('tags')
endpoint.register_urls(api_urls)
endpoint.add_endpoint('tag-list', _(u'Returns a list of all the tags.'))
