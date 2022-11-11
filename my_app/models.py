from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Work(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    postalZip = models.CharField(max_length=40)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

class Accaunt(models.Model):
    pin = models.IntegerField()
    acc_num = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_num