# -*-coding:utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django import forms
from django.contrib.auth.models import User 

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
		form = UserForm(req.POST.get("username"),req.POST.get("pwd"))
		user = User.objects.create_user(req.POST.get("username"),password=req.POST.get("pwd"))
		user.save
		
		
		
	else:
		form=UserForm()
	return render(req,'ldtk/register.html',{})

	
	
	
	
def dashboard(req):
	return render(req,'ldtk/dashboar.html',{})