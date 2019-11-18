from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subjects')

    def __str__(self):
        return self.name 



class Subject2(models.Model):
    what_you_are_teaching=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject2s')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    experience=models.TextField(default='College degree')
    photo=models.ImageField(upload_to='images/', default='blank')
    date_posted=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.what_you_are_teaching

    def get_absolute_url(self):
        return reverse('subject_detail',kwargs={'pk':self.pk})

class Help(models.Model):
    name=models.CharField(max_length=100, default='name')
    subject_name=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.subject_name 

    def get_absolute_url(self):
        return reverse('help_detail',kwargs={'pk':self.pk})