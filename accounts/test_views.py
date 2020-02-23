from django.test import TestCase
from .views import profile, login, update_profile


class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    # def test_get_profile_page(self):
    #     page = self.client.get("/accounts/profile/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "profile.html")
        
    # def test_get_update_page(self):
    #     page = self.client.get("/accounts/update_profile/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "update.html")