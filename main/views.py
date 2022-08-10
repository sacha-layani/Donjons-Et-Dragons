from django.shortcuts import render

from .models import Post
from .models import Contact

from django.http import HttpResponse



def index(request):
    return render(request, 'main/index.html')

def blog(request):
    post = Post.objects.all()
    return render(request, 'main/blog.html', {'post': post})

def article(request, url):
    post = Post.objects.get(url=url)
    return render(request, 'main/article.html', {'post': post})

def download(request):
    return render(request, 'main/download.html')

def contact(request):
    if request.method == "POST":
        contactForm = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactForm.name = name
        contactForm.email = email
        contactForm.message = message
        contactForm.save()
        return HttpResponse("<h2 align='center'>Votre messsage a bien été envoyé :)</h2>")
    return render(request, 'main/contact.html')

# ENGLISH VERSION

def en_index(request):
    return render(request, 'english_version/index.html')

def en_blog(request):
    post = Post.objects.all()
    return render(request, 'english_version/blog.html', {'post': post})

def en_article(request, url):
    post = Post.objects.get(url=url)
    return render(request, 'english_version/article.html', {'post': post})

def en_download(request):
    return render(request, 'english_version/download.html')

def en_contact(request):
    if request.method == "POST":
        contactForm = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactForm.name = name
        contactForm.email = email
        contactForm.message = message
        contactForm.save()
        return HttpResponse("<h2 align='center'>Your message has been sent :)</h2>")
    return render(request, 'english_version/contact.html')


