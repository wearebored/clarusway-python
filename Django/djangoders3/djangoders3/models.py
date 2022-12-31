from django.db import models

# Create your models here.


class Students(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    avatar= models.ImageField(blank=True, null=True,upload_to="student")


    def __str__(self) -> str:
        return self.first_name


class Teacher(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    avatar = models.ImageField(blank=True,null=True,upload_to="teacher")

    def __str__(self) -> str:
        return self.first_name
