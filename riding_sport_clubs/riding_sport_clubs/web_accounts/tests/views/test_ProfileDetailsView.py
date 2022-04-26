from django.test import TestCase
from django.urls import reverse

from riding_sport_clubs.web_accounts.models import Profile, HorseUser


class ProfileDetailsViewTests(TestCase):

    def test_get_profile_details__expect_correct_template(self):
        user = HorseUser.objects.create_user('ivko')

        profile = (Profile(first_name='Ivo', last_name='Ivov', email='ivo@clubs.bg', gender='male',
                               phone_number='+359866012345', user=user),)
        Profile.objects.bulk_create(profile)

        response = self.client.get(reverse('details profile', kwargs={'pk': profile[0].pk}))

        self.assertTemplateUsed(response, 'account/details_profile.html')