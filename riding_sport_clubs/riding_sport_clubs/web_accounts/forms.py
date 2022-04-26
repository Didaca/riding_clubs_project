from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from riding_sport_clubs.web_accounts.models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(
        choices=(
            ('male', 'male'),
            ('female', 'female'),
        ),
    )
    picture = forms.ImageField()
    phone_number = forms.CharField(
        max_length=Profile.PHONE_NUMBER_MAX_LENGTH,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            picture=self.cleaned_data['picture'],
            phone_number=self.cleaned_data['phone_number'],
            user=user,)

        if commit:
            profile.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'gender',
                  'phone_number', 'picture',)
