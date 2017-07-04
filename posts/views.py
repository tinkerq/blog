from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from posts.models import *
from .forms import *
from django.contrib import messages

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Created!")
        return redirect("list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, 'post_create.html', context)

def post_detail(request,post_id):
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "instance": instance,
    "title": "Detail",
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
	object_list = Post.objects.all()
	context = {
	"object_list": object_list,
	"title": "List",
	}
	return render(request, 'post_list.html', context)

def post_update(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance = instance)
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

def post_delete(request,post_id):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("list")