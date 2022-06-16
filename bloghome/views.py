from django.shortcuts import render,HttpResponse
from .models import Blog,Regform
import math

# Create your views here.
def home(request):
    #return HttpResponse("this is my home page")
    return render(request,'index.html')
def blog(request):
    no_of_posts=3 
    page=(request.GET.get('page'))
    if page is None:
        page=1
    else:
        page = int(page)
    print("page=",page)  
    """
    1 : 0 - 3
    2 : 3 - 6
    3 : 6 - 9

    1 : 0 - 0 + no_of posts
    2 : no_of posts to no_of posts+no_of posts
    3 :no_of posts to no_of posts+no_of posts+no_of posts
    (page_no-1)*no_of posts to no_of posts*no_of posts
    """  

    blogs=Blog.objects.all()
    length= len(blogs)
    print("length=",length)
    
    blogs=Blog.objects.all()[(page-1)*no_of_posts: page*no_of_posts]
    print('blog=',blogs)
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page< math.ceil(length/no_of_posts):     
        nxt = page+1 
    else:
        nxt=None  
    print('prev=',prev,'nxt=',nxt)             
    context={'blogs':blogs, 'prev':prev,'nxt':nxt}
    #return HttpResponse("this is my blog page")
    return render(request,'bloghome.html',context)


def contact(request):
    #return HttpResponse("this is my contact page")
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        fullname=request.POST['fullname']
        email=request.POST['email']
        pswd1=request.POST['pswd1']
        pswd2=request.POST['pswd2']
        print(first_name,last_name,fullname,email,pswd1,pswd2)
        ins=Regform(first_name=first_name,last_name=last_name,fullname=fullname,email=email,password=pswd1)
        ins.save()
        print('the data hasbeen saved')
    return render(request,'contact.html')


    
def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    #return HttpResponse(f"you are viewing {slug}")
    return render(request,'blogpost.html',context)    





def search(request):
    #return HttpResponse(f"you are viewing {slug}")
    return render(request,'search.html')        