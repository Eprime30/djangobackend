from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, help_text='Required. Add a valid email address')
    """
    New User Form. Requires password confirmation.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password1',
                  'password2', 'username', 'phone', 'address')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
