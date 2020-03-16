from django.test import TestCase
from django.test import SimpleTestCase
from .forms import UserForm, LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse

class TestLoginForm(SimpleTestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.user ={
            'username': 'andy',
             'password': 'pass@123',
             'email': 'adndy@gmail.com'
        }
    
    def test_the_login_form(self):
        form = LoginForm(data={
            'username': 'andy',
            'password': 'pass@123'
        })
        self.assertTrue(form.is_valid())
        
    def test_the_registration_form(self):
        form = RegistrationForm({
            'username': 'username',
            'email': 'email',
            'password1': 'password1',
            'password2': 'password2'
        })
        self.assertTrue(form.is_valid())
