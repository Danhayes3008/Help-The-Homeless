from django.test import TestCase
from .views import contrabution


class TestViews(TestCase):

    def test_get_contrabution_page(self):
        page = self.client.get("contrabution/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contrabution.html")