from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    address = models.TextField()
    number = models.TextField()
    email = models.EmailField(max_length=30)

    def __str__(self):
        return str(self.name)
