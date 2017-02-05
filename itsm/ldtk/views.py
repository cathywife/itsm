# -*-coding:utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context
from django import forms
from django.contrib.auth.models import User 
from ldtk.models import itsmzsk,shebeileixin
from django.views import generic  
from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout



# Create your views here.

class UserForm(forms.Form):
		name=forms.CharField()
		pwd=forms.CharField()
		

def index(req):
	return render(req,'ldtk/index.html',{})
def home(req):
	if req.method =='POST':
		form = UserForm(req.POST)
	return render(req,'ldtk/home.html',{})

	

	
def register(req):

	if req.method =='POST':
		form = UserForm(req.POST.get("username"),req.POST.get("userpwd"))
		user = User.objects.create_user(req.POST.get("username"),password=req.POST.get("pwd"))
		user.save
		req.method ='GET'
	
		return HttpResponseRedirect("/zsk") 		
	else:
		form=UserForm()
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
	
def zsk(req):
		sblx=shebeileixin.objects.all()
		zskall=itsmzsk.objects.all()
		zsk=itsmzsk.objects.order_by('-shijian')[0:5]
		if req.method=='POST':
			search_test=req.POST.get("text_search")
			
			zsk=itsmzsk.objects.filter(zsk_name__contains=search_test).order_by('-shijian')[0:5]
			return render(req,'ldtk/zsk.html',{'form':zsk,'shebeileixin':sblx,'all':zskall})
			
		
		
		
		
		
		return render(req,'ldtk/zsk.html',{'form':zsk,'shebeileixin':sblx,'all':zskall})

	
	
	
	
def dashboard(req):
	return render(req,'ldtk/dashboar.html',{})