from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class EditarUsuarioForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditarUsuarioForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class RestaurantesForm(forms.ModelForm):

    class Meta:
        model = Restaurantes
        fields = '__all__'
        widgets = {
            'horario_apertura': forms.TimeInput(format='%H:%M'),
            'horario_cierre': forms.TimeInput(format='%H:%M'),
        }


class BaresForm(forms.ModelForm):

    class Meta:
        model = Bares
        fields = '__all__'
        widgets = {
            'horario_apertura': forms.TimeInput(format='%H:%M'),
            'horario_cierre': forms.TimeInput(format='%H:%M'),
        }