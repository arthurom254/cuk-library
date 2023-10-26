from django.shortcuts import render
from .models import School, Course, Unit
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
# Create your views here.

def index(request):
    school = School.objects.all()
    course = Course.objects.all()
    new = Unit.objects.filter()[:10]
    context = {
        "school": school,
        "course": course,
        "new":new,
    }
    return render(request, 'index.html',context)

def units(request, name):
    
    course=Course.objects.get(abbr=name)
    unit=course.unit_set.all()

    context={
        "unit":unit,
        "course":course
    }
    return render(request, 'index2.html', context)

def papers(request, value):
    unit=Unit.objects.get(name=value)
    paper=unit.paper_set.all()
    context={
        "unit":unit,
        "paper":paper
    }
    return render(request,'index3.html', context)


def study(request, value, id):
    unit=Unit.objects.get(name=value)
    paper=unit.paper_set.get(id=id)
    context={
        "unit":unit,
        "paper":paper,
    }
    return render(request,'index4.html',context)

def search(request):
    search=request.GET['q']
    result=Unit.objects.filter(name__icontains=search)
    page_n=request.GET.get('page',1)
    p=Paginator(result, 10)
    try:
        page=p.page(page_n)
    except EmptyPage:
        page=p.page(1)

    context={
        "unit":page,
        "q":search
    }
    return render(request,'search.html',context)
    