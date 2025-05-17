from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class LostItem(models.Model):
    CATEGORY_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='lost')
    found = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    # Only try to save the profile if it exists
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create it
        Profile.objects.create(user=instance)