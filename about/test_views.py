from django.test import TestCase
from .views import about

# This test shows is the page loads or not
class TestViews(TestCase):
    def test_get_about_page(self):
        page = self.client.get("/about_us/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")