from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from riding_sport_clubs.web_clubs.views import HomeView


UserModel = get_user_model()


class HomeViewTests(TestCase):

    def test_get_home_view__when_user_not_logged_in__expect_correct_page(self):
        response = self.client.get(reverse('home page'))

        self.assertEqual(HomeView.conntext_value, response.context[HomeView.context_key])
        self.assertTemplateUsed(response, 'web/home.html')

    def test_get_home_view__when_user_is_logged_in__expect_correct_page(self):
        user_data = {
            'username': 'User',
            'password': '1234',
        }

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('home page'))

        self.assertRedirects(response, reverse('list clubs'))
