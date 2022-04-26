from django import forms

from riding_sport_clubs.web_clubs.models import Club, Trainer


class CreateClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('club_name', 'owner', 'email_club', 'address', 'description', 'club_logo')
        labels = {
            'club_name': 'Club Name',
            'owner': 'Club Owner',
            'email_club': 'Email',
            'address': 'Club Address',
            'description': 'Description',
            'club_logo': 'Club Logo',

        }
        widgets = {
            'owner': forms.TextInput(
                attrs={
                    'placeholder': 'First & Last name'
                },
            ),
        }


class CreateTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('trainer_first_name', 'trainer_last_name', 'trainer_age', 'trainer_info', 'trainer_photo')
        labels = {
            'trainer_first_name': 'First Name',
            'trainer_last_name': 'Last Name',
            'trainer_age': 'Age',
            'trainer_info': 'Trainer info',
            'trainer_photo': 'Picture',
        }
