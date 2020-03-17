
from django.test import TestCase
from .models import Donation

class TestDonationModel(TestCase):
    def test_donation_model_successfull(self):
        name = Donation(name="test")
        name.save()
        self.assertEqual(name.name, "test")
        self.assertFalse(name.done)
