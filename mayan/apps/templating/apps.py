from django.apps import apps
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.menus import menu_list_facet

from .classes import TemplateContextEntry
from .links import link_document_template_sandbox
from .permissions import permission_template_sandbox


class TemplatingApp(MayanAppConfig):
    app_namespace = 'templating'
    app_url = 'templating'
    has_rest_api = True
    has_static_media = True
    has_tests = True
    name = 'mayan.apps.templating'
    verbose_name = _(message='Templating')

    def ready(self):
        super().ready()
        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )

        ModelPermission.register(
            model=Document, permissions=(permission_template_sandbox,)
        )

        menu_list_facet.bind_links(
            links=(link_document_template_sandbox,), sources=(Document,)
        )

        TemplateContextEntry(
            always_available=True,
            description=_(message='Current date and time'), name='now',
            value=timezone.now
        )
