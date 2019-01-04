from django.forms import ModelForm, HiddenInput
from nasagram.models import nasagram


class NasaForm(ModelForm):
    class Meta:
        model = nasagram
        fields = ['comment', 'rating', 'favorite', 'date', 'url']
        widgets = {
            'url': HiddenInput,
            'date': HiddenInput
            }
