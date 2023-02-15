from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    post =Post.objects.get(id=post_id)
    post.delete()
   # output = 'POST ID is'+ str(post_id)
    return HttpResponseRedirect('/')

def likeview(request, post_id):
    new_value=Post.objects.get(id=post_id)
    if(new_value.likes==0):
        new_value.likes+=1
        new_value.save()
        return HttpResponseRedirect('/')
    else:
        new_value.likes-=1
        new_value.save()
        return HttpResponseRedirect('/')

def edit(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')


    return render(request, 'edit.html',
                  {'post': post})
    