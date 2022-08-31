"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 사용자가 index 라는 주소로 요청을 보낸다면
    # articles에 있는 views 파일에서 index 함수를 실행할거야
    # 이 때 함수는 호출하는 것이 아님!!! 함수명만 작성
    path('index/', views.index),
    # 파이썬은 1급 객체이다.
    # 1. 함수를 변수에 저장할 수 있다.
    # 2. 함수를 리턴으로 전달할 수 있다.
    # 3. 함수를 인자로 전달할 수 있다.
    path('hello/', views.hello),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
]
