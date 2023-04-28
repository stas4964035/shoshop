from django import forms
from authapp.models import DealUser
from authapp.forms import DealUserEditForm
from mainapp.models import ListOfCountries
from mainapp.models import Deal


# Форма редактирования параметров пользователя
class DealUserAdminEditForm(DealUserEditForm):
    class Meta:
        model = DealUser
        fields = '__all__'


# Форма редактирования параметров стран
class ListOfCountriesEditForm(forms.ModelForm):
    class Meta:
        model = ListOfCountries
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


# Форма редактирования параметров услуг компании
class DealEditForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
