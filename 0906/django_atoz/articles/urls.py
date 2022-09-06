from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/index/',views.index, name = 'index'),
    path('articles/greeting/',views.greeting, name = 'greeting'),
    path('articles/dinner/', views.dinner, name = 'dinner'),
    path('articles/throw/', views.throw, name = 'throw'),
    path('articles/catch/', views.catch, name = 'catch'),
    path('articles/hello/<str:name>', views.hello, name = 'hello'),

]
