from django.db import models
from django.contrib.auth.models import User 
from django.forms import  ModelForm

# Create your models here.
class itsmsj(models.Model):
	sjid=models.IntegerField(default=0)

	
class gongjuleixin(models.Model):
		name=models.CharField(max_length=30)
		def __str__(self): 
			return self.name
		
class gongju(models.Model):
		name=models.CharField(max_length=20)
		leixin=models.ForeignKey(gongjuleixin,default=1)
		def __str__(self): 
			return self.name 
	
class shebeileixin(models.Model):
		name=models.CharField(max_length=100)
		def __str__(self): 
			return self.name 

class shebei(models.Model):
		name=models.CharField(max_length=100,default='aa')
		sb_lx=models.ForeignKey(shebeileixin,default=1)
		sb_jcsj=models.DateTimeField()
		def __str__(self): 
			return self.name 			

		

class biaoqian(models.Model):
		name=models.CharField(max_length=20)
		def __str__(self): 
			return self.name 
	
class Role(models.Model):
		name=models.CharField(max_length=100)
		person=models.ManyToManyField(User)
	
	
	
class yonghudanwei(models.Model):
		yhdw_name=models.CharField(max_length=100)
		yhdw_address=models.CharField(max_length=100)
		yhdw_Tel=models.IntegerField()
		def __str__(self): 
			return self.name 
		
			

class itsmzsk(models.Model):
		zsk_name=models.CharField(max_length=200)
		zsk_chulifangfan=models.TextField()
		shijian=models.DateTimeField(auto_now_add=True)
		gongju=models.ManyToManyField(gongju)
		jianyirenshu=models.IntegerField(default=1)
		gongxianzhe=models.ForeignKey(User,default=1)
		shebei=models.ForeignKey(shebei,default=1)
		shenpi=models.BooleanField(default=False)
		fabu=models.BooleanField(default=False)
			
		
		def __str__(self): 
			return self.zsk_name 

class zskshenpi(models.Model):
		guandian=models.TextField()
		renyuan=models.ManyToManyField(User)
		zsk=models.ForeignKey(itsmzsk)
		
		time=models.DateTimeField(auto_now=True)
		juedings=(
					('r','reject'),
					('p','pass'),	
				 )
		jueding=models.CharField(max_length=2,
								 choices=juedings,
								 default='r',
								)
		


		
		



		
	
	
class jifang(models.Model):
		danwei=models.ForeignKey(yonghudanwei,default=1)
		weizi=models.CharField(max_length=30)
	
class zichan(models.Model):
			
			jifang=models.ForeignKey(jifang,null=True)
			weizi=models.CharField(max_length=60)
			xinghao=models.CharField(max_length=30)
			sn=models.CharField(max_length=60)
			azsj=models.DateTimeField()
			peizi=models.TextField()
			jcsj=models.DateTimeField()
			ztxz=(('ok','ok'),('dxj','daixunjian'),('gz','guzhang'))
			state=models.CharField(max_length=4,choices=ztxz)


def __str__(zsk_name): 
				return "知识库" 			
			
class zskform(ModelForm):
		class Meta:
			model =	itsmzsk
			fields = ['zsk_name','zsk_chulifangfan','gongju','jianyirenshu','fabu']



class zichanform(ModelForm):
		class Meta:
			model =	zichan
			fields = ['jifang','weizi','xinghao','sn','azsj','peizi','jcsj']
			