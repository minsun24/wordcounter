"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import main.views


#함수 호출하는 부분 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name='main'),   #main 폴더 안에 잇는 views.py에 있는 main 함수를 가져오기
    path('about/', main.views.about, name='about'),
    path('result/', main.views.result, name='result'),
     
]
