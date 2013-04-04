from django import forms
from models import Profile


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        exclude = ('user', 'following')  # User will be filled in by the view.
