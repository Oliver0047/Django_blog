from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404
from . import models
from django.template.context_processors import csrf
# Create your views here.
 
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list': post_list})
 
def Test(request):
    return render(request,'blog/test.html',{'current_time': datetime.now()})
 
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html',{'post':post})

def ListAll(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/list.html', {'post_list': post_list})

def LabelAll(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    post_list = [post.category for post in post_list]
    post_list = list(set(post_list))
    length=len(post_list)
    return render(request, 'blog/label.html', {'post_list': post_list,'length':length})

def AboutMe(request):
    return render(request,'blog/about_me.html')

def userInfo(req):  
    if req.method=="POST":  
        u=req.POST.get("username",None)  
        s=req.POST.get("sex",None)  
        e=req.POST.get("email",None)  
        d=req.POST.get("advice",None)

        info={
            "username":u,  
            "sex":s,  
            "email":e,
            "advice":d,	
        }
        models.UserInfo.objects.create(**info)  
        c=csrf(req)
        info_list=models.UserInfo.objects.all()  
        c.update({"info_list":info_list})
        return render(req,"blog/advice.html",context=c)  
    return render(req,"blog/advice.html",) 
