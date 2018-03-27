from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11,default='')
    receiver = models.CharField(max_length=20,default='')
    address = models.CharField(max_length=100,default='')
