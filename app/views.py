from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
from .models import *
# Create your views here.
def index(request):
    obj=task.objects.all()
    form=task_form()
    if request.method=='POST':
        form=task_form(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            task.objects.create(title=title)
            return redirect('/')

    context={
        'data':obj,
        'form':form
    }
    return render(request,'home.html',context)

def update(request,id):
    obj=task.objects.get(id=id)
    form=task_form(instance=obj)

    if request.method=='POST':
        form=task_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form
    }
    return render(request,'update.html',context)

def delete(request,id):
    obj=task.objects.get(id=id)
    
    if request.method=='POST':
        obj.delete()
        return redirect('/')

    context={
        'data':obj
    }
    return render(request,'delete.html',context)