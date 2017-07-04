from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from posts.models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Created!")
        return redirect("list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, 'post_create.html', context)

def post_detail(request,post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    context = {
    "instance": instance,
    "title": "Detail",
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    context = {
    "object_list": objects,
    "title": "List",
    "user": request.user
    }
    return render(request, 'post_list.html', context)

def post_update(request, post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    form = PostForm(request.POST or None, request.FILES or None,instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Edited!")
        return redirect(instance.get_absolute_url())
    context = {
    "form":form,
    "instance": instance,
    "title": "Update",
    }
    return render(request, 'post_update.html', context)

def post_delete(request,post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("list")