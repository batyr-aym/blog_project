from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, User_site, Coments
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import Post_ser

@login_required
def Get_posts(requests):
    posts = Posts.objects.prefetch_related("coments").select_related("user","user__user_site").all().order_by('-created_time')
    if requests.method == "POST":
        title = requests.POST.get("title")
        description = requests.POST.get('content')
        Posts.objects.create(title=title, user = requests.user, description=description)
        return redirect("get_posts")
        
    return render(requests, 'blog/index.html', {"posts": posts})

@login_required
def Add_Comments(requests, post_id):
    if requests.method == "POST":
        post = get_object_or_404(Posts, id = post_id)
        comments = requests.POST.get("content")
        Coments.objects.create(posts = post, description= comments, user = requests.user)
    return redirect("get_posts")

def Register(requests):
    if requests.method == "POST":
        username = requests.POST.get("username")
        email = requests.POST.get("email")
        password = requests.POST.get("password")
        password2 = requests.POST.get("confirm_password")
        color = requests.POST.get('color')
        if password != password2:
            messages.error(requests, "Пароли не совпадают!")
        elif User.objects.filter(username=username).exists():
            messages.error(requests, "Пользователь с таким ником уже существует!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            User_site.objects.create(user=user, color=color)
            login(requests, user)
            return redirect("get_posts")
    return render(requests, 'autorizations/registration.html')


@login_required
def get_profile(request):
    user_site = get_object_or_404(User_site, user = request.user)
    return render(request, 'blog/profile.html', {"user": request.user, 'user_site': user_site})

@login_required
def update_profile(request):
    if request.method == "POST":
        color = request.POST.get("color")
        user_site = get_object_or_404(User_site, user = request.user)
        user_site.color = color
        user_site.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')

class APIblog(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = Post_ser(posts)
        return Response(serializer.data)