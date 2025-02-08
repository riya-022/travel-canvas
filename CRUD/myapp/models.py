from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class registermodel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=8)
    address = models.TextField()
    profilepicture = models.ImageField(upload_to="photos")
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=10)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.profilepicture.url))

    user_photo.allow_tags = True


class category(models.Model):
    catname = models.CharField(max_length=20)


