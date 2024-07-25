from django import forms
from .models import Account

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Pasword'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "password", "phone_number"]

    def clean(self):
        cleaned_data = super(RegisterationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password Does Not match."
            )