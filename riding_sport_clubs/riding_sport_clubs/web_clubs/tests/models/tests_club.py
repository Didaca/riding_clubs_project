from django.test import TestCase

from riding_sport_clubs.base_validators.validators import VALIDATE_OWNER_NAME_SPACE, VALIDATE_OWNER_NAME
from riding_sport_clubs.web_clubs.models import Club


class ClubTests(TestCase):

    def setUp(self):
        self.club = Club(club_name='Horses', email_club='h@clubs.bg', owner='Ivo Ivov',)

    def test_club_owner_name__when_name_contains_only_letters_for_first_and_last_name_separated__expect_success(self):
        owner_name = 'Ivo Ivov'

        self.assertEqual(owner_name, self.club.owner)

    def test_club_owner_name__when_name_contains_first_and_last_name_not_separated__expect_error(self):
        self.club.owner = 'IvoIvov'
        with self.assertRaises(ValueError) as context:
            self.club.full_clean()
            self.club.save()

        self.assertEqual(VALIDATE_OWNER_NAME_SPACE, str(context.exception))

    def test_club_owner_name__when_name_contains_first_and_last_name_and_digit__expect_error(self):
        self.club.owner = 'Ivo Ivov2'
        with self.assertRaises(ValueError) as context:
            self.club.full_clean()
            self.club.save()

        self.assertEqual(VALIDATE_OWNER_NAME, str(context.exception))
