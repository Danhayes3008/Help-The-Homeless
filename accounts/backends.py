from django.contrib.auth.models import User

# This class checks the email address and password from where the reset email links are sent from
class EmailAuth:
    """Authenticate a user by an exact match on the email and password"""
    def authenticate(self, username=None, password=None):
        """
        Get an instance of `User` based off the email and verify the
        password
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """
        Used by the Django authentiation system to retrieve a user instance
        """        
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None