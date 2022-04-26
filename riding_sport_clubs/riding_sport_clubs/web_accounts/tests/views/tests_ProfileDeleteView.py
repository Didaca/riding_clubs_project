from django.test import TestCase
from django.urls import reverse

from riding_sport_clubs.web_accounts.models import HorseUser, Profile


DELETE_PAGE_MESSAGE = 'Are you sure you want to delete your profile?'


class ProfileDeleteViewTests(TestCase):

    def setUp(self) -> None:
        self.user = HorseUser.objects.create_user('ivko')

        self.profile = (Profile(first_name='Ivo', last_name='Ivov', email='ivo@clubs.bg', gender='male',
                           phone_number='+359866012345', user=self.user),)
        Profile.objects.bulk_create(self.profile)

    def test_get__when_profile_deleted__expect_success(self):

        response = self.client.get(reverse('delete profile', kwargs={'pk': self.profile[0].pk}))

        self.assertContains(response, DELETE_PAGE_MESSAGE)

    def test_post__when_profile_deleted__expect_success(self):

        response = self.client.post(reverse('delete profile', kwargs={'pk': self.profile[0].pk}))

        self.assertRedirects(response, reverse('home page'))

