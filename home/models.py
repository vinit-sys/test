
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="p_images")
    phone_no=models.CharField(max_length=15)
    Address=models.CharField(max_length=350)
    accountType=models.CharField(max_length=30)
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.profile_image.path) # Open image using self

        if img.height > 300 or img.width > 500:
            new_img = (500, 300)
            img.thumbnail(new_img)
            img.save(self.profile_image.path)