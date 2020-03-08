from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    """ หน้าจอแสดงสินค้าที่มีในระบบ """
    

def home(request):
    return render(request, 'POS/index.html')

def show_error_404(request):
    foo = False

    if foo:
        return HttpResponseNotFound('<h1>Not found page.</h1>')
    else:
        return redirect(to='index_home')