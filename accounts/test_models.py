from django.test import TestCase
from .models import Profile

class TestProfileModel(self):
    def test_create_a_profile(self):
        profile = Profile(name="testname")
        profile.save()
        self.assertEqual(profile.name, "testname")
