from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from posts.models import *

def post_create(request):
    context = {
    "title": "Create",
    "user": request.user
    }
    return render(request, 'post_create.html', context)

def post_detail(request):
    instance = get_object_or_404(Post, id=1)
    context = {
    "instance": instance,
    "title": "Detail",
    "user": request.user
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
	object_list = Post.objects.all()
	context = {
	"object_list": object_list,
	"title": "List",
	"user": request.user
	}
	return render(request, 'post_list.html', context)

def post_update(request):
    context = {
    "title": "Update",
    "user": request.user
    }
    return render(request, 'post_update.html', context)

def post_delete(request):
    context = {
    "title": "Delete",
    "user": request.user
    }
    return render(request, 'post_delete.html', context)