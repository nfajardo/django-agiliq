from django.db import models


class Note(models.Model):

    sender = models.CharField(max_length=40)
    recipient = models.CharField(max_length=40)
    msj = models.TextField()
    img = models.ImageField(upload_to='img_notes') 
    created_at = models.DateField(auto_now_add=True)