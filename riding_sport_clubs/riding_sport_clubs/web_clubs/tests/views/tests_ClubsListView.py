from django.test import TestCase
from django.urls import reverse

from riding_sport_clubs.web_clubs.models import Club


class ClubsListViewTests(TestCase):
    image = 'static_files/images/base_image_horse.png'

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list clubs'))

        self.assertTemplateUsed(response, 'web/clubs_list.html')

    def test_get__when_clubs_ordering_descending_by_awards_gold_silver_bronze__expect_ordering_correct(self):

        clubs_to_create = [
            Club(club_name='Eclipse', owner='Ivo Ivov', email_club='eclipse@club.bg', award_gold=3,
                      award_silver=2, award_bronze=2, rating=0, club_logo=self.image),
            Club(club_name='Jokey', owner='Ivo Ivov', email_club='eclipse@club.bg', award_gold=3,
                      award_silver=3, award_bronze=2, rating=0, club_logo=self.image),
        ]

        Club.objects.bulk_create(clubs_to_create)
        ordered_clubs = [
            c for c in Club.objects.order_by('-award_gold', '-award_silver', '-award_bronze',)
        ]

        response = self.client.get(reverse('list clubs'))
        orders = [c for c in response.context['object_list']]

        self.assertEqual(orders, ordered_clubs)
        self.assertTemplateUsed(response, 'web/clubs_list.html')
