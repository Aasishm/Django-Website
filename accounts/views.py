from django.shortcuts import render, HttpResponse
# Create your views here.
# render(request, template_name, dictionaryobject(optional))
def home(request):
    name = 'Aasish'
    age = '22'
    numbers = [1,2,3,4,5]
    return render(request,'accounts/home.html',{'Name':name,'Number':numbers})
