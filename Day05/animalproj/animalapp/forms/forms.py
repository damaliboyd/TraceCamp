from animalapp.models import Animal
from django import forms

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['liked']
        widget = {
            'name' : forms.HiddenInput,
            'age' : forms.HiddenInput,
            'type_of' : forms.HiddenInput,
            'images' : forms.HiddenInput,
            'description' : forms.HiddenInput,
            'location' : forms.HiddenInput,
        }
