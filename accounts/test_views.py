from django.test import TestCase
from django.contrib.auth import SESSION_KEY
from .views import profile, login, update_profile
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_login_page(self):
        def setUp(self):
            self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
            User.objects.create_user(**self.credentials)
        
        page = self.client.get("/accounts/login/", self.credentials, follow=True)
        self.assertEqual(page.status_code, 200)
        response = self.client.post('/login/', **self.credentials)
        self.assertTrue(response.context['user'].is_active)
    
    def test_get_profile_page(self):
        page = self.client.get("/accounts/profile/", self.credentials, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    # def test_get_update_page(self):
    #     page = self.client.get("/accounts/update/")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "update.html")