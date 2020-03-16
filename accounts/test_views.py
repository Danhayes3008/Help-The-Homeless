from django.test import TestCase
from .views import profile, login, update_profile
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile

# this test checks if the login page loads or not
class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")    
    
class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        
class RegisterTest(BaseTest):
    def test_can_view_registration_page(self):
        response=self.client.get(reverse("register"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "registration.html")
        
class ProfileUrl(TestCase):
    def setUp(self):
        self.register_url=reverse('profile')
        self.user ={
            'username': 'andy',
             'password': 'pass@123',
             'email': 'adndy@gmail.com'
        }

class TestprofilePage(BaseTest):
    # def setUp(self):
    #     self.register_url=reverse('profile')
    #     self.user ={
    #         'username': 'andy',
    #          'password': 'pass@123',
    #          'email': 'adndy@gmail.com'
    #     }
                
    def test_profile_page(self):
        page = self.client.get(reverse("profile"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    # def test_history(self):
    #     self.client.login(username='andy', password='pass@123')
    #     # get_history function having login_required decorator
    #     response = self.client.post(reverse('profile'), {'user_id': self.user.id})
    #     self.assertEqual(response.status_code, 200)