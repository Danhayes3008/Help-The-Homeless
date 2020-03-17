
from django.test import TestCase
from .models import Donation

class TestDonationModel(TestCase):
    def test_donation_model_successfull(self):
        name = Donation(name="test")
        name.save()
        self.assertEqual(name.name, "test")
    
    def test_donation_model_fail(self):
        name = Donation(name="test")
        name.save()
        self.assertFalse(name.name, "hello")
