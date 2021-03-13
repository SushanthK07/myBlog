from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact
import math

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    no_of_posts = 3
    # print(request.GET.get('page'))
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        # by default, request.GET.get() returns string
        page = int(page)
    # print(page)
    """
    1 : 0 to no_of_posts
    2 : no_of_posts to no_of_posts + no_of_posts
    3 : no_of_posts + no_of_posts to no_of_posts + no_of_posts + no_of_posts

    (page - 1) * no_of_posts to page * no_of_posts 
    """
    
    all_blogs = Blog.objects.all()
    length = len(all_blogs)

    blogs = Blog.objects.all()[(page - 1) * no_of_posts : page * no_of_posts]
    
    if page > 1:
        prev = page - 1
    else:
        prev = None
    
    if page < math.ceil(length / no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    # first() gives the first post among the posts that have same slug
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}

    return render(request, 'blogpost.html', context)
    # return HttpResponse(f"You are viewing {slug}")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()

    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
