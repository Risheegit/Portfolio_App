from django.db import models
from PIL import Image

# Create your models here.
class Startup (models.Model):
    startup_name = models.CharField(max_length = 50)
    description = models.TextField(blank = True, null =True)
    industry = models.CharField(max_length=50, blank = True, null = True)
    logo = models.ImageField(upload_to = 'logos', default = 'default.jpg')
    website = models.CharField(max_length=50, blank = True, null =True) 
    def __str__(self) :
        return self.startup_name

