from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from posts.models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.utils import timezone
from django.db.models import Q

# def usersignup(request):
#     context={}
#     form = UserSignup()
#     context['form']=form
#     if request.method == "POST":
#         form=UserSignup(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username=user.username
#             password=user.password
#             user.set_password(password)
#             user.save()
#             auth_user= authenticate(username=username, password=password)
#             login(request,auth_user)


def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.save()
        messages.success(request, "Successfully Created!")
        return redirect("list")
    context = {
    "title": "Create",
    "form": form,
    }
    return render(request, 'post_create.html', context)

def post_detail(request,post_slug):
    instance = get_object_or_404(Post, slug=post_slug)
    if instance.publish>timezone.now().date() or instance .draft:
        if not (request.user.is_staff or request.user.is_superuser):
            raise Http404
    context = {
    "title": "Detail",
    "instance": instance,
    "share_string": quote(instance.content)
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    today = timezone.now().date()
    object_list = Post.objects.filter(draft=False).filter(publish__lte=today)
    if request.user.is_staff or request.user.is_superuser:
        object_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)
            ).distinct()

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    context = {
    "object_list": objects,
    "title": "List",
    "user": request.user,
    "today": today
    }
    return render(request, 'post_list.html', context)

def post_update(request, post_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
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
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    instance = get_object_or_404(Post, slug=post_slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("list")