from django.db import models

# Create your models here.

class college(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='photo')
    desc=models.TextField()
    icon=models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name

class teacher(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    decs=models.TextField()

    def __str__(self):
        return self.name