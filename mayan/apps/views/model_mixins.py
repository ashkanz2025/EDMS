from django.apps import apps
from django.utils.translation import gettext_lazy as _

from .literals import LIST_MODE_CHOICES


class ModelMixinUserViewModeBusinessLogic:
    def get_app_config(self):
        app_config = apps.get_app_config(app_label=self.app_label)
        return app_config

    get_app_config.help_text = _(message='The app to which the view belongs.')
    get_app_config.short_description = _(message='App')

    def get_value_display(self):
        map_list_mode_choices = dict(LIST_MODE_CHOICES)

        try:
            return map_list_mode_choices[self.value]
        except KeyError:
            return _(message='Unknown mode: %s') % self.value

    get_value_display.help_text = _(message='The current mode of the view.')
    get_value_display.short_description = _(message='Value')
