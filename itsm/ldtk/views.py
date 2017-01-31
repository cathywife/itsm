# -*-coding:utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context


# Create your views here.
def index(req):
    #t = loader.get_template('ldtk/index.html');
    #c=Context({})
	return render(req,'ldtk/index.html',{})