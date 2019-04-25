from django.db import models
# Create your models here.
class Userinfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    userimage_url=models.CharField(max_length=50)
    usertype=models.CharField(max_length=20)
class Project(models.Model):
    project_name=models.CharField(max_length=30)
    project_ver=models.CharField(max_length=10)
    project_url=models.TextField()
    type=((0,'启用'),(1,'禁用'))
    project_type=models.IntegerField(choices=type)
    create_time=models.DateTimeField(auto_now_add=True)
    project_remark=models.TextField()
class API(models.Model):
    project=models.ForeignKey('Project',on_delete=models.PROTECT)
    API_name=models.CharField(max_length=30)
    API_url=models.TextField()
    API_para=models.TextField()
    API_remark=models.TextField()
    ways=((0,'POST'),(1,'GET'))
    API_way=models.IntegerField(choices=ways)
    create_time = models.DateTimeField(auto_now_add=True)
class interface(models.Model):
   API=models.ForeignKey('API',on_delete=models.PROTECT)
   interface_name=models.CharField(max_length=50)
   interface_result=models.TextField()
   interface_remark=models.TextField()
   interface_rel_result=models.TextField()
   create_time = models.DateTimeField(auto_now_add=True)

class API_result(models.Model):
    reslut_name=models.CharField(max_length=50)
