from django import forms

from exam.models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        # fields = ['brand_name', 'serial_number', 'cover', 'description']
        exclude = ['created_at']

