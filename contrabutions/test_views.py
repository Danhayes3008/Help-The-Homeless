from django.test import TestCase
from .views import contribution

# This test checks if the page loads
class TestViews(TestCase):

    def test_get_contribution_page(self):
        page = self.client.get("/contribution/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contribution.html")