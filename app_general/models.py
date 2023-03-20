from django.db import models

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.

class BookingModel(models.Model):
    quantity = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='imageluggage/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
@receiver(post_delete, sender=BookingModel)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)
    except:
        pass

@receiver(pre_save, sender=BookingModel)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = BookingModel.objects.get(id=instance.id).image

        try:
            new_img = instance.image
        except:
            new_img = None

        if new_img != old_img:
            if old_img is not None:
                old_img.delete(save=False)
    except:
        pass