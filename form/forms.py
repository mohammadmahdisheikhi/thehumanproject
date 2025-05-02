from django import forms
from register.models import CustomUser, Gender, UserResponse

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'first_name', 'last_name', 'age', 'gender', 'country', 'city']
        widgets = {
            'gender': forms.Select(choices=Gender.choices),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # No need for city queryset logic anymore — both are CharFields now
        # You may optionally set placeholders or input styles here if desired


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }
