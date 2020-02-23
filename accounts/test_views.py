from django.test import TestCase
from .views import profile, login


class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")