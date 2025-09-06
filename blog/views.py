from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    
    context = {
        'posts': posts
    }
    
    return render(request, 'home.html', context)