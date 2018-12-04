from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import math

# Post.objects.all().delete()
num_posts_per_page = 8

def index(request):
    print("inside views.index")
    posts = Post.objects.all()
    print("# of posts:", len(posts))
    pages = []
    for i in range(1, math.ceil(len(posts)/num_posts_per_page)+1):
        pages.append(i)
    context = {
        'posts' : posts[0:8],
        'pages' : pages
    }
    # for key in request.session.keys():    # <-- (iterating through session dictionary)
    #     print(key, request.session[key])

    return render(request, "myapp/index.html", context)

def create(request):
    print("inside views.create")
    # print(request.POST)
    Post.objects.create(post=request.POST['post'])
    return redirect('/')

@csrf_exempt
def posts_api(request):
    print("inside views.posts_api")
    # print(request.POST)
    Post.objects.create(post=request.POST['post'])
    posts = Post.objects.all()
    print("number of posts:", len(posts))
    pages = []
    for i in range(1, math.ceil(len(posts)/num_posts_per_page)+1):
        pages.append(i)
    context = {
        'posts': posts,
        'pages': pages
    }
    return render(request, 'myapp/posts.html', context)

@csrf_exempt
def load(request, page_num):
    print(request.POST)
    print("inside views.load_page")
    posts = Post.objects.all()
    min = (int(page_num)-1) * num_posts_per_page
    max = min + num_posts_per_page
    print("min", min)
    print("max", max)
    pages = []
    for i in range(1, math.ceil(len(posts)/num_posts_per_page)+1):
        pages.append(i)
    context = {
        'posts': posts[min:max],
        'pages': pages
    }
    return render(request, 'myapp/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')

@csrf_exempt
def get_page(request):
    print("inside views.get_page")
    print(request.POST) # e.g. <QueryDict: {'3': ['']}>

    # for key in request.POST.keys():
    #     page_num = key

    page_num = int(request.POST['page_num'])

    posts = Post.objects.all()
    min = (int(page_num)-1) * num_posts_per_page
    max = min + num_posts_per_page
    print("min", min)
    print("max", max)
    pages = []
    for i in range(1, math.ceil(len(posts)/num_posts_per_page)+1):
        pages.append(i)
    context = {
        'posts': posts[min:max],
        'pages': pages
    }
    return render(request, 'myapp/posts.html', context)
    # return redirect('/')
