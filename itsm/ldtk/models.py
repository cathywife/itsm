from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class itsmsj(models.Model):
	sjid=models.IntegerField(default=0)

	
class gongjuleixin()
		name=models.CharField(max_length=30)
		
class gongju(models.Model):
		name=models.CharField(max_length=20)
		leixin=models.ForeignKey(gongjuleixin)
	
class shebeileixin(models.Model):
		name=models.CharField(max_length=100)
		

class biaoqian(models.Model):
	name=models.CharField(max_length=20)
	
class user_group(models.Model):
	ug_name=models.CharField(max_length=100)
	
	
class yonghudanwei(models.Model):
		yhdw_name=models.CharField(max_length=100)
		yhdw_address=models.CharField(max_length=100)
		yhdw_Tel=models.IntegerField()
		
		

class yonghu(models.Model):
		yh_name=models.CharField(max_length=50)
		yh_psw=models.CharField(max_length=20)
		yh_phone=models.IntegerField()
		yh_address=models.CharField(max_length=100)
		yh_dan=models.ForeignKey(yonghudanwei)
		yh_descripition=models.CharField(max_length=100)
		yh_birthday=models.DateTimeField()

class itsmzsk(models.Model):
		zsk_name=models.CharField(max_length=200)
		zsk_chulifangfan=models.CharField(max_length=500)
	


class itsmwt(models.Model):
		wt_name=models.CharField(max_length=100)
		


		

class fuwufanwei(models.Model):
		fwfw_name=models.CharField(max_length=100)


class xjitem(models.Model):
		xjitem_name=models.CharField(max_length=100)
		xjitem_group=models.ForeignKey(fuwufanwei)
		

		
class shebei(models.Model):
		sb_lx=models.ForeignKey(shebeileixin)
		sb_jcsj=models.DateTimeField()

		
class peizhiku(models.Model):
		pz_iitem=models.ForeignKey(shebei)
		pz_user = models.CharField(max_length=100)
		pz_pwd  = models.CharField(max_length=100)
	
class weizhi(models.Model):
        wz_shen=models.CharField(max_length=30)
	
class jifang(models.Model):
		jf_danwei=models.ForeignKey(yonghudanwei)
		jf_gly=models.ForeignKey(yonghu)
		jf_weizhi=models.ForeignKey(weizhi)
		
class jigui(models.Model):
		jg_jf=models.ForeignKey(jifang)
		jg_weizhi=models.CharField(max_length=100)


