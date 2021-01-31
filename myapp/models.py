from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=200)
    product_description=models.CharField(max_length=1000)
    product_price=models.CharField(default="",max_length=25)
    fuel=models.CharField(default="",max_length=25)
    year=models.CharField(max_length=20,default="")
    kilometers_driven=models.CharField(default="",max_length=20)
    image_1=models.ImageField(upload_to="myapp/images/",blank=True)
    image_2=models.ImageField(upload_to="myapp/images/",blank=True)
    image_3=models.ImageField(upload_to="myapp/images/",blank=True)
    image_4=models.ImageField(upload_to="myapp/images/",blank=True)
    image_5=models.ImageField(upload_to="myapp/images/",blank=True)
    image_6=models.ImageField(upload_to="myapp/images/",blank=True)
    image_7=models.ImageField(upload_to="myapp/images/",blank=True)
    image_8=models.ImageField(upload_to="myapp/images/",blank=True)
    image_9=models.ImageField(upload_to="myapp/images/",blank=True)
    image_10=models.ImageField(upload_to="myapp/images/",blank=True)
    date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.product_name
    