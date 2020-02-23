from django.test import TestCase
from .views import profile


class TestViews(TestCase):

    def test_get_profile_page(self):
        page = self.client.get("/accounts")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")