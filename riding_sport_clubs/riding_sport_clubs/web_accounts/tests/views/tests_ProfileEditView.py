from django.test import TestCase
from django.urls import reverse

from riding_sport_clubs.web_accounts.models import HorseUser, Profile


class ProfileEditViewTests(TestCase):

    def test_post__when_profile_changes__expect_success(self):
        user = HorseUser.objects.create_user('ivko')

        profile = (Profile(first_name='Ivo', last_name='Ivov', email='ivo@clubs.bg', gender='male',
                           phone_number='+359866012345', user=user),)
        Profile.objects.bulk_create(profile)

        response = self.client.post(reverse('edit profile', kwargs={'pk': profile[0].pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/edit_profile.html')
