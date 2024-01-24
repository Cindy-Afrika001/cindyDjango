from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
      return self.firstname+" "+self.lastname

class product(models.Model):
    productid = models.IntegerField(default=0)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.productname