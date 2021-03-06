"""api_program URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from api_project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.User_Login.as_view()),
    path('home/',views.home),
    path('logout/',views.logout),
    path('project/',views.Project.as_view()),
    path('API/',views.API.as_view()),
    path('Interface/',views.Interface.as_view()),
    path('report/',views.Generate_Report),
    path('Interface_set/',views.Interface_set.as_view()),
    re_path('Interface_set/detail/(\d+)',views.detail),
    path('set/',views.set),
    path('start/',views.start_run),
    path('user/',views.User.as_view()),
]
