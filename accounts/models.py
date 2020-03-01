from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    name = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    image = models.ImageField(default="blankProfileImage.png", upload_to='images', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False, force_update=False):
        
        super(Profile, self).save(force_insert, force_update)

        if self.id is not None:
            previous = Profile.objects.get(id=self.id)
            if self.image and self.image != previous.image:
                images = image.open(self.Profile.path)
                images = images.resize((96, 96), image.ANTIALIAS)
                images.save(self.logo.path)
    
@receiver(post_save, sender=User)
def create_or_update_user_profile (sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()