from django import forms
from .models import Medicine
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(MedicineForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if field.errors:
                    field.widget.attrs.update({'class': 'error'})


class RegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
