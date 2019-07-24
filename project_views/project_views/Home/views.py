from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def Blog(request):
    isi = blog.objects.all()
    return render(request, 'Blog.html',{'isi': isi})

def mentee(request):
    isi = Mentee.objects.all()
    return render(request, 'Mentee.html', {'isi': isi})

def mentor(request):
    isi = Mentor.objects.all()
    return render(request, 'Mentor.html', {'isi': isi})

def Author(request):
    return render(request, 'Author.html')

def inputblog(request):
    if request.method == "POST":
        form = InputBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputBlog()
    return render(request, 'inputblog.html', {'form': form})

def inputmentee(request):
    if request.method == "POST":
        form = InputMentee(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputMentee()
    return render(request, 'inputmentee.html', {'form': form})

def inputmentor(request):
    if request.method == "POST":
        form = InputMentor(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputMentor()
    return render(request, 'inputmentor.html', {'form': form})