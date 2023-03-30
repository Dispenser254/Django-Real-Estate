from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name