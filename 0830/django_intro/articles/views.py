import random
from django.shortcuts import render

# 첫 번째 인자로 request 를 받아야 함
# 사용자의 요청 정보가 request에 들어있음
def index(request):
    # 딕셔너리
    context = {
        'ssafy': 'Hello SSAFY!',
        'age' : 20,
        'lunch' : ['라멘', '갈치조림', ]
    }
    return render(request, 'index.html', context)


def hello(request):
    return render(request, 'hello.html')


def dinner(request):
    foods = ['햄버거', '피자', '치킨', '짜장면']
    pick = random.choice(foods)

    context = {
        'foods': foods,
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def throw(request):
    return render(request, 'input.html')


def catch(request):
    # print(type(request.GET.get('a1'))) # get 방식으로 보낸 데이터를 확인할 수 있음
    context = {
        'name': request.GET.get('n1'),
        'age': request.GET.get('a1')
    }
    return render(request, 'name.html', context)