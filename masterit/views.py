from django.shortcuts import render,redirect
from .models import Category,Subject,Subject2,Help
from .forms import Subject2Form,HelpForm
from django.contrib.auth.decorators import login_required
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

@login_required
def subject2_create(request):
    if request.method == 'POST':
        form = Subject2Form(request.POST)
        if form.is_valid():
            subject2 = form.save()
            return redirect('subject2_detail', pk=subject2.pk)
    else:
        form = Subject2Form()
    return render(request, 'masterit/subject2_form.html', {'form': form})

@login_required
def help_create(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            help = form.save()
            return redirect('help_detail', pk=help.pk)
    else:
        form = HelpForm()
    return render(request, 'masterit/help_form.html', {'form': form})