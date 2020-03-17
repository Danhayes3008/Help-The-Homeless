from django.test import TestCase
from .views import profile, login, update_profile
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile
from accounts.forms import RegistrationForm

# this test checks if the login page loads or not
class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")    
    
class BaseTest(TestCase):
    def setUp(self):
        self.user={
            'username': 'username',
            'password1': 'password1',
            'password2': 'password2',
            'email': 'testemail@gmail.com'
            
        }
        self.register_url=reverse('register')
        self.profile_url=reverse('profile')
        
class RegisterTest(BaseTest):
    def test_can_view_registration_page(self):
        response=self.client.get(reverse("register"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "registration.html")
        
    def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)
        
class ProfileTest(BaseTest):
    def test_if_the_profile_page_loads(self):
        response=self.client.get(self.profile_url,self.user)
        self.assertEqual(response.status_code,302)
        self.assertTemplateUsed(response, "profile.html")
        