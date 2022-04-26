from django.test import TestCase

from riding_sport_clubs.base_validators.validators import VALIDATE_NAME, VALIDATE_PLUS, VALIDATE_NUMBER
from riding_sport_clubs.web_clubs.models import Trainer


class TrainerTests(TestCase):
    def setUp(self):
        self.trainer = Trainer(trainer_first_name='Ivo', trainer_last_name='Ivov', trainer_age=33,
                               trainer_phone_number='+359866012345')

    def test_first_name__when_name_contains_only_letters__expect_success(self):
        first_name = 'Ivo'

        self.assertEqual(first_name, self.trainer.trainer_first_name)

    def test_first_name__when_name_not_contains_only_letters__expect_error(self):
        self.trainer.trainer_first_name = 'Ivo_'

        with self.assertRaises(ValueError) as contex:
            self.trainer.full_clean()
            self.trainer.save()

        self.assertEqual(VALIDATE_NAME, str(contex.exception))

    def test_last_name__when_name_contains_only_letters__expect_success(self):
        last_name = 'Ivov'

        self.assertEqual(last_name, self.trainer.trainer_last_name)

    def test_last_name__when_name_not_contains_only_letters__expect_error(self):
        self.trainer.trainer_last_name = 'Ivov '

        with self.assertRaises(ValueError) as contex:
            self.trainer.full_clean()
            self.trainer.save()

        self.assertEqual(VALIDATE_NAME, str(contex.exception))

    def test_phone_number__when_number_correct__expect_success(self):
        number = '+359866012345'

        self.assertEqual(number, self.trainer.trainer_phone_number)

    def test_phone_number__when_number_not_start_with_plus__expect_error(self):
        self.trainer.trainer_phone_number = '359866012345'

        with self.assertRaises(ValueError) as context:
            self.trainer.full_clean()
            self.trainer.save()

        self.assertEqual(VALIDATE_PLUS, str(context.exception))

    def test_phone_number__when_number_not_contains_only_digit__expect_error(self):
        self.trainer.trainer_phone_number = '+359866_012345'

        with self.assertRaises(ValueError) as context:
            self.trainer.full_clean()
            self.trainer.save()

        self.assertEqual(VALIDATE_NUMBER, str(context.exception))
