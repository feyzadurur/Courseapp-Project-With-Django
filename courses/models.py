from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(default="",null=False,unique=True,db_index=True,max_length=50)

    def __str__(self):
        return f"{self.name}"
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super().save(args,kwargs)


class Course(models.Model):
    title=models.CharField(max_length=50,null=True)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50,blank=True)
    date=models.DateField(auto_now=True)
    isActive=models.BooleanField()
    slug=models.SlugField(default="",blank=True,editable=False,null=False,unique=True,db_index=True)

    #category=models(Category,default=1,on_delete=models.CASCADE,related_name="kurslar")
    categories=models.ManyToManyField(Category)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title} {self.date}"
    

