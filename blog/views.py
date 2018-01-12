from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    '''
    context = {
        'title':'Latest Posts',
        'posts':post
    } then pass in render instead of the current dictionary'''
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})




"""
def details(request,id):
    post = Posts.objects.get(id=id)
    contexxt = {
        'post':post
    }
    return render(request, 'posts/details.html', context)
"""

