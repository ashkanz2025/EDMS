from django.utils.html import conditional_escape

from mayan.apps.forms import forms


class TagFormWidget(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        result = super().create_option(
            attrs=attrs, index=index,
            label='{}'.format(
                conditional_escape(text=label)
            ), name=name, selected=selected, subindex=subindex,
            value=value
        )

        result['attrs']['data-color'] = value.instance.color

        return result
