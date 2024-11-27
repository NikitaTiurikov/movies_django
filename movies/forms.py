from django import forms
from .models import Registration


class AddRegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['login', 'name', 'pwd']

class AddLogInForm(forms.Form):
    login = forms.CharField(max_length=255, label='Логін')
    pwd = forms.CharField(max_length=255, label='Пароль')

class FilterForm(forms.Form):
    filter_by_country = forms.ChoiceField(required=False, choices=((1, "Україна"), (0, "не Україна")), label="Обрати країну")


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(required=False, choices=((1, "ім'ям"), (2, "рейтингом")), label="Сортувати за")