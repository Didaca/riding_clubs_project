from django.test import TestCase
from django.urls import reverse


class ClubCreateViewTests(TestCase):

    def test_create_club__expect_success_created(self):
        response = self.client.post(reverse('create club'))

        self.assertTemplateUsed(response, 'web/create_club.html')
