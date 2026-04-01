from django.db import models

from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length = 100)
    birthdate = models.DateField(null = True,blank = True)

    def _str_(self):
        return self.name
    
class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.ForeignKey(Author,on_delete= models.CASCADE)
        summary = models.TextField()
        isbn = models.CharField(max_length=13,unique=True)
        published_date = models.DateField(auto_now_add=True)
        price = models.DecimalField(max_digits=6,decimal_places=2)
        def _str_(self):
              return self.title
        
        def get_absolute_url(self):
            return reverse('book-detail',args = [str(self.id)])    