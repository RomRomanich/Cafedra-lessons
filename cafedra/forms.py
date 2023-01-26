from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import Select

from .models import *
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class AddLessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['name', 'text', 'tezkorlik', 'datetime']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.TextInput(attrs={'class': 'input', 'label': 'area'}),
            'types': forms.TextInput(attrs={'type': 'list'}),
            'datetime': DateTimeWidget(attrs={'id': "yourdatetimeid"}),
        }

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AddReferatForm(forms.ModelForm):
    class Meta:
        model = Referat
        fields = ['title', 'author', 'text', 'datetime']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'author': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.TextInput(attrs={'class': 'input'}),
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                                   'data-target': '#datetimepicker1'}),
        }

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

