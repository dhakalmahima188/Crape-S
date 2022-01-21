from django.db import models

# Create your models here.
class files(models.Model):
    title = models.CharField(max_length=200)
    file = models.BinaryField()
    institution=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    
    #check??
    #make folder attribute by yourself
    language=models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    creation_date = models.CharField(max_length=200)
    preview = models.BinaryField()

   


#parameters_add
# institution(url parse)
# url
# title_actual
# published date
#1at 5 pages preview



