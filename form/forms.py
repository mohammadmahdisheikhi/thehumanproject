# --- form/forms.py ---
from django import forms
from register.models import CustomUser, Gender, UserResponse
from django.utils.translation import gettext_lazy as _


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'first_name', 'last_name', 'age', 'gender', 'country', 'city']
        widgets = {
            'gender': forms.Select(choices=Gender.choices),
        }
        labels = {
            'phone': _('Phone Number'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'age': _('Age'),
            'gender': _('Gender'),
            'country': _('Country'),
            'city': _('City'),
        }


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'text': _('Response'),
        }