from django.db import models


# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    confirmpassword = models.CharField(max_length=12)
    name = models.CharField(max_length=122)
    dob = models.CharField(max_length=12)
    gender = models.CharField(max_length=1)
    city = models.CharField(max_length=10)
    
    
    
class Login(models.Model):
    loginusername = models.CharField(max_length=100)
    loginpassword = models.CharField(max_length=12)

class Profile(models.Model):
    upload = models.ImageField(upload_to='images/')
    
    
    

    def __str__(self):
        return self.name