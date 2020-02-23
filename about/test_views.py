from django.test import TestCase
from .views import about


class TestViews(TestCase):

    def test_get_about_page(self):
        page = self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")