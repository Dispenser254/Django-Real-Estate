from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

def __str__(self):
    return self.name

class Meta:
    verbose_name="Contact"
    verbose_name_plural="Contacts"