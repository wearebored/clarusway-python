from django.db import models

# Create your models here.

class Students(models.Model):
    number= models.CharField(max_length=10)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.first_name