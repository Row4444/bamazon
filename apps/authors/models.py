from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Author's name")
    last_name = models.CharField(max_length=64, verbose_name="Author's last name")
    image = models.ImageField(null=True, blank=True, upload_to='authors/images/')
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def str(self):
        return "{} {}".format(self.first_name, self.last_name)


@receiver(pre_save, sender=Author)
def pre_save_author(sender, instance, update_fields, **kwargs):
    if instance.date_of_death >= timezone.now().date():
        instance.date_of_death = None
    if instance.date_of_birth >= timezone.now().date():
        raise ValidationError("Date of birth mast be in past.")

