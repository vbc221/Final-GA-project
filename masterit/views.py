from django.shortcuts import render
from .models import Category,Subject,Subject2,Help
# Create your views here.

def category_list(request):
    categories=Category.objects.all()
    return render(request,'masterit/category_list.html',{'categories':categories})


def category_detail(request,pk):
    category=Category.objects.get(id=pk)
    return render(request,'masterit/category_detail.html',{'category':category})

def subject_detail(request,pk):
    subject=Subject.objects.get(id=pk)
    return render(request,'masterit/subject_detail.html',{'subject':subject})

def subject2_detail(request,pk):
    subject2=Subject2.objects.get(id=pk)
    return render(request,'masterit/subject2_detail.html',{'subject2':subject2})

def help_list(request):
    helps=Help.objects.all()
    return render(request,'masterit/help_list.html',{'helps':helps}) 

def help_detail(request,pk):
    help=Help.objects.get(id=pk)
    return render(request,'masterit/help_detail.html',{'help':help})