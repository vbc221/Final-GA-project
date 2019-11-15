from django.db import models

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
    name=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject2s')
    teacher=models.CharField(max_length=100, default='name')
    
    def __str__(self):
        return self.name

class Help(models.Model):
    name=models.CharField(max_length=100)
    subject_name=models.CharField(max_length=100)
    body=models.CharField(max_length=300)

    def __str__(self):
        return self.subject_name 