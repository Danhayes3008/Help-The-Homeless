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
    
    
# class TestProfileViews(TestCase):
#     self.user = User.objects.create(username='andy', password='pass@123', email='adndy@gmail.com')
#     self.client = Profile()

#     def test_history(self):
#         self.client.login(username=self.user.username, password='pass@123')
#         # get_history function having login_required decorator
#         response = self.client.post(reverse('profile'), {'user_id': self.user.id})
#         self.assertEqual(response.status_code, 200)