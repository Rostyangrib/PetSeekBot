from .models import Pet
from django.forms import ModelForm, TextInput

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', "age", 'idshka']

        widgets = {
            "name": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "breed": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Порода'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "idshka": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id'
            }),
        }