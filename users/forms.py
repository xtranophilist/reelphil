from django import forms
from models import Profile
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile



attrs_dict = {
# 'class': 'required'
}


class UserRegistrationForm(RegistrationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))

    def save(self, profile_callback=None):
        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['email'])

        new_profile = Profile(user=new_user, full_name=self.cleaned_data['full_name'])
        new_profile.save()

        return new_user


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        exclude = ('user', 'following')  # User will be filled in by the view.
