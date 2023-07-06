from django.db import models

class products(models.Model):
    productName = models.CharField(max_length=250,null=False,blank=False),
    productPrice = models.IntegerField(blank=False,null=False),
    image1 = models.ImageField(upload_to='static/img/'),
    image2 = models.ImageField(upload_to='static/img/'),
    image3 = models.ImageField(upload_to='static/img/'),
    image4 = models.ImageField(upload_to='static/img/'),
    quantityAvailable = models.IntegerField(),
    brand = models.CharField(max_length=250),
    productDescription = models.TextField(),