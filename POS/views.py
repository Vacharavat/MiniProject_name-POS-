from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from POS.models import Product, Product_type


# Create your views here.
def my_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'รหัสผิดนะจ๊ะ'

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')


def home(request):

    search_product = request.GET.get('search_product', '')
    search_type = request.GET.get('search_type', '')
    
    po_type = Product_type.objects.all().order_by('id')
    pos = Product.objects.all()

    if request.method == 'GET':
        if search_product != '' and search_type != '':
            pos = Product.objects.filter(name__icontains=search_product, Type=search_type)
        elif search_product != '':
            pos = Product.objects.filter(name__icontains=search_product)

    return render(request, 'POS/index.html', context={
        'search_product': search_product,
        'pos': pos,
        'po_type': po_type
    })


# def AddToChart(request, pos_id):
#     context = {}
#     print(pos_id)
#     return render(request, template_name='POS/cart.html', context=context)


def Management(request):
    msg = ''
    po_type = Product_type.objects.all().order_by('id')


    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            Type=request.POST.get('Type'),
            price=request.POST.get('price'),
        )
        msg = 'สร้างสินค้าใหม่ได้แล้ว: %s' % (product.name)
    else:
        product = Product.objects.none()

    context = {
        'type': po_type,
        'product': product,
        'msg': msg
    }

    return render(request, 'POS/management.html', context=context)

def ManagementType(request):
    msg = ''

    if request.method == 'POST':
        Type = Product_type.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        msg = 'สร้างประเภทใหม่ได้แล้ว: %s' % (Type.name)
    else:
        Type = Product_type.objects.none()

    context = {
        'Type': Type,
        'msg': msg
    }

    return render(request, 'POS/management.html', context=context)




def show_error_404(request):
    foo = False

    if foo:
        return HttpResponseNotFound('<h1>Not found page.</h1>')
    else:
        return redirect(to='index_home')


