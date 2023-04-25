from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, \
    UserCreationForm

from .models import DealUser, DealUserProfile


class DealUserRegisterForm(UserCreationForm):
    class Meta:
        model = DealUser
        fields = (
            'username', 'first_name', 'password1',
            'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class DealUserEditForm(UserChangeForm):
    class Meta:
        model = DealUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("ВЫ слишком молоды!")

        return data


class DealUserLoginForm(AuthenticationForm):
    class Meta:
        model = DealUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(DealUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DealUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = DealUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(DealUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
