from django.utils.translation import gettext_lazy as _

from mptt.exceptions import InvalidMove
from rest_framework.exceptions import ValidationError
from rest_framework.reverse import reverse
from rest_framework_recursive.fields import RecursiveField

from mayan.apps.documents.models.document_type_models import DocumentType
from mayan.apps.documents.permissions import permission_document_type_edit
from mayan.apps.rest_api import serializers
from mayan.apps.rest_api.relations import FilteredPrimaryKeyRelatedField

from ..models import IndexTemplate, IndexTemplateNode


class IndexTemplateNodeSerializer(serializers.ModelSerializer):
    children = RecursiveField(
        label=_(message='Children'), many=True, read_only=True
    )
    index_url = serializers.SerializerMethodField(
        label=_(message='Index URL'), read_only=True
    )
    parent_url = serializers.SerializerMethodField(
        label=_(message='Parent URL'), read_only=True
    )
    url = serializers.SerializerMethodField(
        label=_(message='URL'), read_only=True
    )

    # DEPRECATION: Version 5.0, remove 'parent' from GET fields as this
    # is replaced by 'parent_id'.
    # DEPRECATION: Version 5.0, remove 'index' from GET fields as this
    # is replaced by 'index_id'.
    class Meta:
        fields = (
            'children', 'enabled', 'expression', 'id', 'index', 'index_id',
            'index_url', 'level', 'link_documents', 'parent', 'parent_id',
            'parent_url', 'url'
        )
        model = IndexTemplateNode
        read_only_fields = (
            'children', 'id', 'index', 'index_id', 'index_url', 'level',
            'parent_id', 'parent_url', 'url'
        )

    def get_index_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.index.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplate-detail'
        )

    def get_parent_url(self, obj):
        if obj.parent and not obj.parent.is_root_node():
            return reverse(
                format=self.context['format'], kwargs={
                    'index_template_id': obj.index.pk,
                    'index_template_node_id': obj.parent.pk
                }, request=self.context['request'],
                viewname='rest_api:indextemplatenode-detail'
            )
        else:
            return ''

    def get_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.index.pk,
                'index_template_node_id': obj.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplatenode-detail'
        )


class IndexTemplateNodeWriteSerializer(serializers.ModelSerializer):
    children = RecursiveField(
        label=_(message='Children'), many=True, read_only=True
    )
    index_url = serializers.SerializerMethodField(
        label=_(message='Index URL'), read_only=True
    )
    parent = FilteredPrimaryKeyRelatedField(
        label=_(message='Parent')
    )
    parent_url = serializers.SerializerMethodField(
        label=_(message='Parent URL'), read_only=True
    )
    url = serializers.SerializerMethodField(
        label=_(message='URL'), read_only=True
    )

    class Meta:
        fields = (
            'children', 'enabled', 'expression', 'id', 'index', 'index_url',
            'level', 'link_documents', 'parent', 'parent_url', 'url'
        )
        model = IndexTemplateNode
        read_only_fields = (
            'children', 'id', 'index', 'index_url', 'level', 'parent_url',
            'url'
        )

    def create(self, validated_data):
        validated_data['index'] = self.context['index_template']
        return super().create(validated_data=validated_data)

    def get_index_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.index.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplate-detail'
        )

    def get_parent_queryset(self):
        return self.context['index_template'].index_template_nodes.all()

    def get_parent_url(self, obj):
        if obj.parent:
            return reverse(
                format=self.context['format'], kwargs={
                    'index_template_id': obj.index.pk,
                    'index_template_node_id': obj.parent.pk
                }, request=self.context['request'],
                viewname='rest_api:indextemplatenode-detail'
            )
        else:
            return ''

    def get_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.index.pk,
                'index_template_node_id': obj.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplatenode-detail'
        )

    def update(self, instance, validated_data):
        try:
            return super().update(
                instance=instance, validated_data=validated_data
            )
        except InvalidMove as exception:
            raise ValidationError(detail=exception)


class IndexTemplateSerializer(serializers.HyperlinkedModelSerializer):
    document_types_url = serializers.HyperlinkedIdentityField(
        help_text=_(
            message='URL of the API endpoint showing the list document types '
            'associated with this index template.'
        ), label=_(message='Document types URL'),
        lookup_url_kwarg='index_template_id',
        view_name='rest_api:indextemplate-documenttype-list'
    )
    document_types_add_url = serializers.HyperlinkedIdentityField(
        help_text=_(
            message='URL of the API endpoint to add document types '
            'to this index template.'
        ), label=_(message='Document types add URL'),
        lookup_url_kwarg='index_template_id',
        view_name='rest_api:indextemplate-documenttype-add'
    )
    document_types_remove_url = serializers.HyperlinkedIdentityField(
        help_text=_(
            message='URL of the API endpoint to remove document types '
            'from this index template.'
        ), label=_(message='Document types remove URL'),
        lookup_url_kwarg='index_template_id',
        view_name='rest_api:indextemplate-documenttype-remove'
    )
    index_template_root_node_id = serializers.PrimaryKeyRelatedField(
        label=_(message='Index template root node ID'),
        source='index_template_root_node', read_only=True
    )
    nodes_url = serializers.SerializerMethodField(
        label=_(message='Nodes URL'), read_only=True
    )
    rebuild_url = serializers.HyperlinkedIdentityField(
        label=_(message='Rebuild URL'), lookup_url_kwarg='index_template_id',
        view_name='rest_api:indextemplate-rebuild',
    )
    reset_url = serializers.HyperlinkedIdentityField(
        label=_(message='Reset URL'), lookup_url_kwarg='index_template_id',
        view_name='rest_api:indextemplate-reset',
    )
    url = serializers.SerializerMethodField(
        label=_(message='URL'), read_only=True
    )

    class Meta:
        extra_kwargs = {
            'document_types': {
                'label': _(message='Document types'),
                'lookup_url_kwarg': 'document_type_id',
                'view_name': 'rest_api:documenttype-detail'
            }
        }
        fields = (
            'document_types_add_url', 'document_types_url',
            'document_types_remove_url', 'enabled', 'id',
            'index_template_root_node_id', 'label', 'nodes_url',
            'rebuild_url', 'reset_url', 'slug', 'url'
        )
        model = IndexTemplate
        read_only_fields = (
            'document_types_add_url', 'document_types_url',
            'document_types_remove_url', 'id', 'index_template_root_node_id',
            'nodes_url', 'rebuild_url', 'reset_url', 'url'
        )

    def get_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplate-detail'
        )

    def get_nodes_url(self, obj):
        return reverse(
            format=self.context['format'], kwargs={
                'index_template_id': obj.pk
            }, request=self.context['request'],
            viewname='rest_api:indextemplatenode-list'
        )


class DocumentTypeAddSerializer(serializers.Serializer):
    document_type = FilteredPrimaryKeyRelatedField(
        help_text=_(
            message='Primary key of the document type to add to the index '
            'template.'
        ), label=_(message='Document type ID'), source_model=DocumentType,
        source_permission=permission_document_type_edit
    )


class DocumentTypeRemoveSerializer(serializers.Serializer):
    document_type = FilteredPrimaryKeyRelatedField(
        help_text=_(
            message='Primary key of the document type to remove from the '
            'index template.'
        ), label=_(message='Document type ID'), source_model=DocumentType,
        source_permission=permission_document_type_edit
    )
