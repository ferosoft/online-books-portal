from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sir Arthur Conan Doyle',
        'title': 'The Hound of the Baskervilles',
        'about': 'The Hound of the Baskervilles is the third of the four crime novels written by Sir Arthur Conan Doyle featuring the detective Sherlock Holmes'

    },
    {
        'author': 'Sir Arthur Conan Doyle',
        'title': 'The Hound of the Baskervilles',
        'about': 'The Hound of the Baskervilles is the third of the four crime novels written by Sir Arthur Conan Doyle featuring the detective Sherlock Holmes'

    }
]
def index(request):
    context = {
        'post' : posts,
        'title': 'Books'
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title':'About Us'
    }
    return render(request,'blog/about.html',context)

def contact(request):
    context = {
        'title':'Contact Information'
    }
    return render(request,'blog/contact.html',context)

def register(request):
    context = {
        'title':'Register with Us'
    }
    return render(request,'blog/register.html',context)