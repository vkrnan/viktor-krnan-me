from django.db import models

# Create your models here.

class List(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True, upload_to="images/")
    date = models.DateField(auto_now=False, null=False)

class Content(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, upload_to="images/")
    post = models.ForeignKey(List, on_delete=models.CASCADE)

