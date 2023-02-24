from django.db import models

# Create your models here.
class FIRSTAPPLICATION(models.Model):
    Name = models.CharField(255)
    ID = models.IntegerField()
    contact = models.IntegerField()
    Address = models.CharField(255)






