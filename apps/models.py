from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
	name=models.CharField(max_length=255)
	contact=models.CharField(max_length=255,blank=True,null=True)

	def __str__(self):
		return self.name 

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255)
    cover=models.ImageField(upload_to="uploads/book/",null=True,blank=True)
    # pdf=models.FileField(upload_to="uploads/book/pdf/",null=True,blank=True)
    author=models.ForeignKey(Author,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
