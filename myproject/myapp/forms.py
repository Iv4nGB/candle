from django import forms
from django.core.exceptions import ValidationError
from . import models


class AddMasterClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].label = 'Имя'
        self.fields['customer_phone'].label = 'Номер телефона'

    class Meta:
        model = models.MasterClass
        fields = ['customer_name', 'customer_phone']

        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': '*введите имя', 'class': 'input1'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': '*введите номер', 'class': 'input2'}),
        }


class AddGiftCertificate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].label = 'Имя'
        self.fields['customer_phone'].label = 'Номер телефона'

    class Meta:
        model = models.GiftCertificate
        fields = ['customer_name', 'customer_phone']

        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': '*введите имя', 'class': 'input1'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': '*введите номер', 'class': 'input2'}),
        }