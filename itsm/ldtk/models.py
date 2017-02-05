from django.db import models
from django.contrib.auth.models import User 

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
	
class user_group(models.Model):
	ug_name=models.CharField(max_length=100)
	
	
	
class yonghudanwei(models.Model):
		yhdw_name=models.CharField(max_length=100)
		yhdw_address=models.CharField(max_length=100)
		yhdw_Tel=models.IntegerField()
		def __str__(self): 
			return self.name 
		
		

class yonghu(models.Model):
		yh_name=models.CharField(max_length=50)
		yh_psw=models.CharField(max_length=20)
		yh_phone=models.IntegerField()
		yh_address=models.CharField(max_length=100)
		yh_dan=models.ForeignKey(yonghudanwei,default=1)
		yh_descripition=models.CharField(max_length=100)
		yh_birthday=models.DateTimeField()
		

class itsmzsk(models.Model):
		zsk_name=models.CharField(max_length=200)
		zsk_chulifangfan=models.CharField(max_length=500)
		shijian=models.DateTimeField(auto_now_add=True)
		gongju=models.ManyToManyField(gongju)
		jianyirenshu=models.IntegerField(default=1)
		gongxianzhe=models.ForeignKey(User,default=1)
		shebei=models.ForeignKey(shebei,default=1)
		shenpi=models.BooleanField(default=False)
		fabu=models.BooleanField(default=False)
		
		
		
		def __str__(self): 
			return self.zsk_name 
	


class itsmwt(models.Model):
		wt_name=models.CharField(max_length=100)
		


		

class fuwufanwei(models.Model):
		fwfw_name=models.CharField(max_length=100)


class xjitem(models.Model):
		xjitem_name=models.CharField(max_length=100)
		xjitem_group=models.ForeignKey(fuwufanwei,default=1)
		

		

	 

		
class peizhiku(models.Model):
		pz_iitem=models.ForeignKey(shebei,default=1)
		pz_user = models.CharField(max_length=100)
		pz_pwd  = models.CharField(max_length=100)
	
class weizhi(models.Model):
        wz_shen=models.CharField(max_length=30)
	
class jifang(models.Model):
		jf_danwei=models.ForeignKey(yonghudanwei,default=1)
		jf_gly=models.ForeignKey(yonghu,default=1)
		jf_weizhi=models.ForeignKey(weizhi,default=1)
		
class jigui(models.Model):
		jg_jf=models.ForeignKey(jifang,default=1)
		jg_weizhi=models.CharField(max_length=100)


