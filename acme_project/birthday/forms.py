from django import forms
from .models import Birthday
from .validators import real_age

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['first_name', 'last_name', 'birthday']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
    
    # Дополнительная валидация
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if f'{first_name} {last_name}' in BEATLES:
            raise forms.ValidationError('Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!')
