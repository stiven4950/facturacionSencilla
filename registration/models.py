from django.db import models
from django.contrib.auth.models import User
# Paquetes de DJango necesarios para incorporar las señales
from django.dispatch import receiver
from django.db.models.signals import post_save

# Una función que cambia el comportamiento por defecto del upload_to
# El objetivo es ayduar a ahorrar la mayor cantidad de espacio disponible
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, default='')
    identity = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)