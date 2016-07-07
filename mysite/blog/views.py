from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def post_list(request):
    posts = Post.objects
    return render(request, 'blog/post_list.html', {'posts': posts})
