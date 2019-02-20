from django.shortcuts import render
from .models import *
from django.http import HttpResponse,FileResponse,Http404
from django.views.generic import ListView,DetailView

def post_list(request):
    return render(request,'first/home.html')

def contact(request):
    return render(request, 'first/basic.html',{'content':['If you would like to contact me, please email me.','rahulbhatanagar40@gmail.com']})


def pdf_view(request):
    try:
        return FileResponse(open('object/Rahul_Bhatanagar.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def blog(request):
    a=Programming.objects.all()
    return render(request,'first/blog.html',{'blog':a})

def detail(request,menu):
    a=Programming.objects.get(slug=menu)
    n=a.name
    a=[i for i in a.value.split('\n')]
    return render(request,'first/detail.html',{'detail':a,'n':n})
    
