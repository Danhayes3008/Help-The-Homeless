from django.test import TestCase
from django.test import SimpleTestCase
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User

class TestLoginForm(SimpleTestCase):
    self.user = User.objects.create(username='andy', password='pass@123', email='adndy@gmail.com')
    
    def test_the_login_form(self):
        form = LoginForm(data={
            'username': 'andy',
            'password': 'pass@123'
        })
        self.assertTrue(form.is_valid())