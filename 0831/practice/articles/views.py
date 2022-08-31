from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def greeting(request):
    return render(request, 'greeting.html', {'name' = 'Alice'})
def throw(request):
    return render(request, 'throw.html')
def catch(request):
    pass
    return render(request, 'catch.html')
def hello(reuest, name):
    context = {
        'name' = name,
        
    }
    return render(reuqest,'hello html',context)