from django.db import models

# Create your models here.
class files(models.Model):
    title = models.CharField(max_length=200)
    file = models.BinaryField()
    #check??
    #make folder attribute by yourself
    uploaded_at = models.DateTimeField(auto_now_add=True)




