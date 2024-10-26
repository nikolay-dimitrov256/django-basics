from django import forms

from worldOfSpeedApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileCreateForm(ProfileBaseForm):
    pass
