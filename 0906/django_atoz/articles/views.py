from django.shortcuts import render
import random
# Create your views here.
def index(request):
    render(request, 'articles/index.html')

def greeting(request):
    foods = ['chicken', 'pizza', 'coffee']
    name = {
        'name' : 'Jonghyeok'
    }
    context = {
        'foods' : foods,
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)
def dinner(request):
    foods = ['냉면', '보쌈', '고추바사삭']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'articles/dinner.html', context)
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)

def hello(request,name):
    context = {
        'name' : name,
    }
    return render(request,'articles/hello.html', context)