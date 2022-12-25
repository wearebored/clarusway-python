from django.db import models

# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    age=models.IntegerField()
    sinif=models.IntegerField()
    number=models.IntegerField()
    about=models.TextField(blank=True,null=True )
    register= models.DateTimeField(auto_now_add=True)
    last_update_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.number} {self.first_name}"

    class  Meta:
        ordering=["number"]
        verbose_name_plural="Öğrenciler"