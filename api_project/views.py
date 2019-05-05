from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from api_project import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from django.contrib import auth
from django.http import QueryDict
import requests
from django.core.cache import cache
# Create your views here.
class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('is_login'):
            response = super(BaseView, self).dispatch(request, *args, **kwargs)
            return response
        else:
            return redirect('/login/')
class User_Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        ecode_message={}
        username=request.POST.get('username')
        password=request.POST.get('password')
        value=models.Userinfo.objects.filter(username=username,password=password)
        print(value)
        if value:
            request.session['username']=username
            request.session['is_login']=True
            request.session.set_expiry(0)
            ecode_message['ecode']=0
            ecode_message['message']='登录成功'
            return HttpResponse(json.dumps(ecode_message))
        else:
            ecode_message['ecode']=1
            ecode_message['message']='登录失败'
            return HttpResponse(json.dumps(ecode_message))
def logout(request):
    auth.logout(request)
    return redirect('/login')

def home(request):
    is_login=request.session.get('is_login',None)
    if is_login:
        username=request.session.get('username',None)

        return render(request,'home.html',{'username':username})
    else:
        return redirect('/login')
class Project(BaseView):
    def get(self,request):
        project_name=request.GET.get('projectname')
        if project_name:
            project=models.Project.objects.filter(project_name__contains=project_name)
        else:
            project=models.Project.objects.all().order_by('create_time')
        paginator=Paginator(project,10)
        page=request.GET.get('page')
        username = request.session.get('username', None)
        try:
            contacts=paginator.page(page)
        except PageNotAnInteger:
            contacts=paginator.page(1)
        except EmptyPage:
            contacts=paginator.page(paginator.num_pages)
        return render(request,'home.html',{"project":contacts,"username":username})
    def post(self,request):
        ecode_message = {}
        projectname=request.POST.get('projectname')
        projectver=request.POST.get('projectver')
        projecturl=request.POST.get('projecturl')
        projecttype=request.POST.get('projecttype')
        projectremark=request.POST.get('projectremark')
        id=request.POST.get('project-id')
        if id:
            models.Project.objects.filter(id=id).update(project_name=projectname,project_ver=projectver,project_url=projecturl,project_type=projecttype,project_remark=projectremark)
            ecode_message['ecode'] = 0
            return HttpResponse(json.dumps(ecode_message))
        else:
            if projectname and projecturl:
                models.Project.objects.create(project_name=projectname,project_ver=projectver,project_url=projecturl,project_type=projecttype,project_remark=projectremark)
                ecode_message['ecode']=0
                return HttpResponse(json.dumps(ecode_message))
            else:
                ecode_message['ecode']=1
                return  HttpResponse(json.dumps(ecode_message))
    def put(self,request):
        body=QueryDict(request.body)
        project_type=body.get('project_type')
        project_id=body.get('p-id')
        print(project_type,type(project_id))
        if int(project_type) == 1:
            models.Project.objects.filter(id=project_id).update(project_type=0)
        else:
            models.Project.objects.filter(id=project_id).update(project_type=1)
        return HttpResponse(json.dumps(1))

    def delete(self,request):
        pid=QueryDict(request.body)
        id=pid.get('id')
        models.Project.objects.filter(id=id).delete()
        return HttpResponse(json.dumps(1))
class API(BaseView):
    def get(self,request):
        username=request.session.get('username',None)
        project_name=models.Project.objects.filter(project_type=0)
        API=models.API.objects.all()
        painator=Paginator(API,10)
        page=request.GET.get('page')
        try:
            contacts=painator.page(page)
        except PageNotAnInteger:
            contacts=painator.page(1)
        except EmptyPage:
            contacts=painator.page(painator.num_pages)
        return render(request,'API.html',{'username':username,"project_name":project_name,"API":contacts})
    def post(self,request):
        ecode_message={}
        print(request.body)
        API_id=request.POST.get('API-id')
        Project_id=int(request.POST.get("project_name"))
        API_name=request.POST.get("API_name")
        API_url=request.POST.get("API_url")
        API_way=request.POST.get("API_way")
        API_para=request.POST.get("API_para")
        API_remark=request.POST.get("API_remark")
        print(API_id)
        if API_id:
            ecode_message['ecode'] = 0
            ecode_message["message"] = "编辑成功"
            models.API.objects.filter(id=API_id).update(project_id=Project_id, API_name=API_name, API_url=API_url, API_way=API_way,
                                      API_para=API_para, API_remark=API_remark)
            return HttpResponse(json.dumps(ecode_message))
        else:
            if Project_id and API_name:
                ecode_message['ecode']=0
                ecode_message["message"]="新增成功"
                models.API.objects.create(project_id=Project_id,API_name=API_name,API_url=API_url,API_way=API_way,API_para=API_para,API_remark=API_remark)
                return HttpResponse(json.dumps(ecode_message))
            else:
                ecode_message['ecode'] = 1
                ecode_message["message"] = "新增失败"
                return  HttpResponse(json.dumps(ecode_message))
    def delete(self,request):
        ecode_message={}
        body=QueryDict(request.body)
        API_id=body.get('API_id')
        print(API_id)
        models.API.objects.filter(id=API_id).delete()
        ecode_message['ecode'] = 0
        ecode_message["message"] = "删除成功"
        return  HttpResponse(json.dumps(ecode_message))
    def put(self,request):
        headers={"appication/json"}
        body=QueryDict(request.body)
        API_id=body.get('API_id')
        API_token=body.get('API_token')
        headers['token']=API_token
        API=models.API.objects.filter(id=API_id).first()
        if API.way==0:
            r=requests.post(url=API.API_url,data=API.API_para,headers=headers)
            print(r.json())
class Interface(BaseView):
        def get(self,request):
            username=request.session.get("username")
            API=models.API.objects.all()
            Interfa=models.interface.objects.all()
            painator=Paginator(Interfa,10)
            page = request.GET.get('page')
            try:
                Interface = painator.page(page)
            except PageNotAnInteger:
                Interface = painator.page(1)
            except EmptyPage:
                Interface = painator.page(painator.num_pages)
            return render(request,'Interface.html',{"Interface":Interface,"API":API,"username":username})
        def post(self,request):
            ecode_meassge={}
            interface_id=request.POST.get("interface_id")
            API_id=request.POST.get("API_name")
            Interface_name=request.POST.get("Interface_name")
            Interface_remark=request.POST.get("Interface_remark")
            Interface_result=request.POST.get("Interface_result")
            if interface_id:
                if Interface_name:
                    models.interface.objects.filter(id=interface_id).update(API_id=API_id,
                                                                            interface_name=Interface_name,
                                                                            interface_remark=Interface_remark,
                                                                            interface_result=Interface_result)
                    ecode_meassge["ecode"] = 0
                    ecode_meassge["message"] = "编辑成功"
                    return HttpResponse(json.dumps(ecode_meassge))
                else:
                    ecode_meassge["ecode"] = 1
                    ecode_meassge["message"] = "用例名称不能为空"
                    return HttpResponse(json.dumps(ecode_meassge))

            else:
                if Interface_name:
                    models.interface.objects.create(API_id=API_id,interface_name=Interface_name,interface_remark=Interface_remark,interface_result=Interface_result)
                    ecode_meassge["ecode"]=0
                    ecode_meassge["message"]="新增成功"
                    return HttpResponse(json.dumps(ecode_meassge))
                else:
                    ecode_meassge["ecode"]=1
                    ecode_meassge["message"]="用例名称不能为空"
                    return HttpResponse(json.dumps(ecode_meassge))
        def put(self,request):
            info={}
            interface=QueryDict(request.body)
            id=interface.get('interface_id')
            interface_info=models.interface.objects.filter(id=id).first()
            info["interface_name"]=interface_info.interface_name
            info["interface_result"]=interface_info.interface_result
            info["interface_remark"]=interface_info.interface_remark
            info["API_id"]=interface_info.API_id
            print(info)
            return HttpResponse(json.dumps(info))

        def delete(self,request):
            ecode_message={}
            interface=QueryDict(request.body)
            id=interface.get("Interface_id")
            print(id)
            models.interface.objects.filter(id=id).delete()
            ecode_message["ecode"]=0
            return HttpResponse(json.dumps(ecode_message))

def Generate_Report(request):
    headers={}
    Interface = QueryDict(request.body)
    Interface_id = Interface.get("Interface_id")
    API_token = Interface.get("API_token")
    API_id = models.interface.objects.filter(id=Interface_id).first()
    Interface_reslut = API_id.interface_result
    API_url = API_id.API.API_url
    API_way = API_id.API.API_way
    API_para = API_id.API.API_para
    print(API_url,API_way,API_para)
    if API_way == 0:
        r = requests.post(API_url, data=API_para)
        reslut = r.json()
        if reslut['eCode']!=0 or reslut['httpStatus']!=200:
            reslut["result"]="测试不通过"
            models.interface.objects.filter(id=Interface_id).update(interface_rel_result=reslut['result'])
            print(reslut)
            return HttpResponse(json.dumps(reslut))

class Interface_set(BaseView):
    def get(self,request):
        result=models.API_result.objects.all()
        for i in result:
            print(i.reslut_name)
        username=request.session.get('username')
        return render(request,'interface_set.html',{"username":username,"result":result})
    def post(self,request):
        message = {}
        name=request.POST.get("set_name")
        mark=request.POST.get("set_mark")
        id=request.POST.get("set_id",None)
        if id:
            models.API_result.objects.filter(id=id).update(reslut_name=name,reslut_remark=mark)
            message["ecode"] = 0
            return HttpResponse(json.dumps(message))
        else:
            if name:
                models.API_result.objects.create(reslut_name=name,reslut_remark=mark)
                message["ecode"]=0
                return HttpResponse(json.dumps(message))
            else:
                message["eocde"]=0
                return HttpResponse(json.dumps(message))
    def put(self,request):
        message={}
        result=QueryDict(request.body)
        id=result.get("id")
        print(id)
        result=models.API_result.objects.filter(id=id).first()
        message["name"]=result.reslut_name
        message["mark"]=result.reslut_remark
        return HttpResponse(json.dumps(message))
    def delete(self,request):
        message=dict()
        result=QueryDict(request.body)
        id=result.get("id")
        models.API_result.objects.filter(id=id).delete()
        message["eocde"] = 0
        return HttpResponse(json.dumps(message))
def detail(request,id):
    result = models.API_result.objects.all()
    result_all=models.API_result.objects.filter(id=id).first()
    interface=result_all.interface.all()
    inter=models.interface.objects.all()
    username = request.session.get('username')
    return render(request, 'interface_set.html', {"username": username, "result": result,"interface":interface,"inter":inter})
def set(request):
    id=request.POST.get('id')
    inter_id=request.POST.get('list')
    set=models.API_result.objects.filter(id=id).first()
    print(inter_id)
    for r in inter_id:
        if r.isdigit():
            print(r)
            a=models.interface.objects.get(id=int(r))
            set.interface.add(a)
    return HttpResponse(json.dumps("12"))
def start_run(request):
    id=request.POST.get('id')
    set_id=models.API_result.objects.filter(id=id).first()
    inter=set_id.interface.all()
    for i in inter:
        r=requests.post(i.API.API_url,data=i.API.API_para,headers={"content/type":"application/json"})
        models.interface.objects.filter(id=i.id).update(interface_rel_result=r.json())
    return HttpResponse(json.dumps("1"))
class User(BaseView):
    def get(self,request):
        user=models.Userinfo.objects.all()
        painator=Paginator(user,10)
        page = request.GET.get('page')
        try:
            user = painator.page(page)
        except PageNotAnInteger:
            user = painator.page(1)
        except EmptyPage:
            user = painator.page(painator.num_pages)
        username = request.session.get('username')
        return render(request, 'user.html', {"username": username,"user":user})