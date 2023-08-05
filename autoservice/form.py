from .models import Client
from django.forms import ModelForm, TextInput


class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = ["ClientName", "ClientPhone", "ClientCar"]
        widgets = {
            'ClientName': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите ваше имя'
            }),
            'ClientPhone': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите номер телефона'
            }),
            'ClientCar': TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Введите название вашего автомобиля'
            }),
        }
