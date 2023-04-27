from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def student(request):
    SO=studentform()
    d={'SO':SO}
    if request.method=='POST':
        SD=studentform(request.POST)
        if SD.is_valid():
            return HttpResponse(str(SD.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'student.html',d)