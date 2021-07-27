from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class All(models.Model):
    user_email = models.EmailField(max_length=254)
    user_phone = PhoneNumberField(null=False, blank=False, unique=True)
    user_name = models.CharField(max_length=200)
    user_surname = models.CharField(max_length=200)
    user_birthday = models.DateField()

    def __str__(self):
        return self.user_name

class Post(models.Model):
    author = models.CharField(max_length=200)
    author_email = models.EmailField(max_length=254)
    publish_date = models.DateField()


