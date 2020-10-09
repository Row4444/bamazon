from django.db import models


# Create your models here.


class Settings(models.Model):
    title = models.CharField(max_length=64, verbose_name='title text on index')
    hallow_text = models.TextField(verbose_name='hallow text on index')
    description = models.TextField(verbose_name='description about bamazone')

    def save(self):
        self.pk = 1
        return super(Settings, self).save()
