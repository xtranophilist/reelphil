from django import forms
from models import Profile


class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            exclude = ('user',)  # User will be filled in by the view.
