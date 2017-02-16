# -*-coding:utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context
from django import forms
from django.contrib.auth.models import User 
from ldtk.models import itsmzsk,shebeileixin,zskform,zichanform
from django.views import generic  
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth





# Create your views here.

class UserForm(forms.Form):
		name=forms.CharField()
		pwd=forms.CharField()
		

def index(req):
	return render(req,'ldtk/index.html',{})
def home(req):
		if req.method =='POST':
			user = authenticate(username=req.POST['username'],password=req.POST['userpwd'])
			if	user is not None:
				login(req,user)
				return HttpResponseRedirect("/zsk") 
			else:
				return	render(req,'ldtk/client.html',{})
		else:	
			return render(req,'ldtk/home.html',{'form':zskform})

	

	
def register(req):

	if req.method =='POST':
		
		if req.POST.get("userpwd1")!=req.POST.get("userpwd2"):
			return render(req,'ldtk/register.html',{})
		else:
			
			form = UserForm(req.POST.get("username"),req.POST.get("userpwd"))
			user = User.objects.create_user(req.POST.get("username"),password=req.POST.get("pwd"))
			user.set_password(req.POST.get("userpwd1"))
			user.first_name=req.POST.get("firstname")
			user.last_name=req.POST.get("lastname")
			
			user.save
			req.method ='GET'
		
			return HttpResponseRedirect("/zsk") 		
	else:
		return render(req,'ldtk/register.html',{})
	

def client(req):

	if req.method =='POST' :
		 user = authenticate(username=req.POST.get("username"),password=req.POST.get("userpwd"))
		 if	user is not None :
				User.login(req,user)
				return HttpResponseRedirect("/zsk") 		
	else:
		form=UserForm()
	return render(req,'ldtk/client.html',{})

	
def zaijian(request):
		logout(request)
		return render(request,'ldtk/logout.html',{}) 
		
		
		
def zskn(req,a):
		if req.method=='POST':
			return zsk(req)
		zskn=itsmzsk.objects.filter(id=a)
		return render(req,'ldtk/zskxx.html',{'form':zskn})

		
	
def zsk(req):
		sblx=shebeileixin.objects.all()
		zskall=itsmzsk.objects.all()
		zsk=itsmzsk.objects.order_by('-shijian')
		if req.method=='POST':
			search_test=req.POST.get("text_search")			
			zsk=itsmzsk.objects.filter(zsk_name__contains=search_test).order_by('-shijian')[0:5]
			return render(req,'ldtk/zsk.html',{'form':zsk,'shebeileixin':sblx,'all':zskall})		
		return render(req,'ldtk/zsk.html',{'form':zsk,'shebeileixin':sblx,'all':zskall})

	
	
	
	
def dashboard(req):
	return render(req,'ldtk/dashboar.html',{})