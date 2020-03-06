from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# This model creates the profile table 
class Profile(models.Model):
    name = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    image = models.ImageField(default="blankProfileImage.png", upload_to='images', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'
    # this def is an attempt to resize images when the profile is updated to resolve the issue where they look either stretched or squashed
    def save(self, force_insert=False, force_update=False, *args, **kwargs,):        
        super(Profile, self).save(force_insert, force_update, *args, **kwargs)
        if self.id is not None:
            previous = Profile.objects.get(id=self.id)
            if self.image and self.image != previous.image:
                images = images.open(self.Profile.path)
                images = images.resize((225, 225), images.ANTIALIAS)
                images.save(self.logo.path)
# This section creates a profile for the user when an account is made
@receiver(post_save, sender=User)
def create_or_update_user_profile (sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()