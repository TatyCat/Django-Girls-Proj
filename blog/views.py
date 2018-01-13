from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    '''
    context = {
        'title':'Latest Posts',
        'posts':post
    } then pass in render instead of the current dictionary
    '''
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

"""
commit=False means that we don't want to save the Post model yet 
    – we want to add the author first. 
Most of the time you will use form.save() without commit=False

def details(request,id):
    post = Posts.objects.get(id=id)
    contexxt = {
        'post':post
    }
    return render(request, 'posts/details.html', context)
"""

