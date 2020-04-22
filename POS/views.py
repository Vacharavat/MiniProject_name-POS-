from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from POS.models import Order, Order_Products, Product, Product_type


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

@login_required
def home(request):
    
    """ หน้าแรกของเว็บเพจที่จะแสดงถึงรายกสินค้าและตะกร้าที่สามารถนำสินค้าเข้าไปได """

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

@login_required
def management(request):
    
    """ หน้าจัดการร้านค้า ที่สามารถเพิ่ม ลบ แก้ สินค้าหรือประเภทได้ """

    search_product = request.GET.get('search_product', '')
    search_type = request.GET.get('search_type', '')
    
    po_type = Product_type.objects.all().order_by('id')
    pos = Product.objects.all()

    if request.method == 'GET':
        if search_product != '' and search_type != '':
            pos = Product.objects.filter(name__icontains=search_product, Type=search_type)
        elif search_product != '':
            pos = Product.objects.filter(name__icontains=search_product)

    return render(request, 'POS/management.html', context={
        'search_product': search_product,
        'pos': pos,
        'po_type': po_type
    })
@login_required
def product_add(request):
    
    """ สำหรับเพิ่มสินค้าเข้าไปในดาต้าเบส """


    msg = ''
    po_type = Product_type.objects.all().order_by('id')
    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            Type_id=request.POST.get('Type'),
            price=request.POST.get('price'),
        )
        msg = 'สร้างสินค้าใหม่ได้แล้ว: %s' % (product.name)
    else:
        product = Product.objects.none()

    context = {
        'po_type': po_type,
        'product': product,
        'msg': msg
    }

    return render(request, 'POS/product_add.html', context=context)
@login_required
def type_add(request):
    
    """ สำหรับเพิ่มประเภทใหม่เข้าไปในดาต้าเบส """

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
        'product_type': Type,
        'msg': msg
    }

    return render(request, 'POS/add_type.html', context=context)
@login_required
def product_edit(request, product_id):
    
    """ สำหรับแก้สินค้าในดาต้าเบส"""

    try:
        product = Product.objects.get(pk=product_id)
        product_type = Product_type.objects.all()
        msg = ''
    except Product.DoesNotExist:
        return redirect('management')
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.Type_name = request.POST.get('Type')
        product.price = request.POST.get('price')
        product.save()
        msg = 'แก้ไขสินค้าสำเร็จแล้ว: %s' %(product.name)
    
    context = {
        'po_type': product_type,
        'product': product,
        'msg': msg
    }


    return render(request, 'POS/product_add.html', context=context)
@login_required
def product_delete(request, product_id):

    """ สำหรับลบสินค้าในดาต้าเบส """
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect(to='management')

@login_required
def type_manage(request):
    
    """ หน้าจัดการประเภทสินค้า ที่สามารถ ลบ แก้ ประเภทได้ """

    
    po_type = Product_type.objects.all().order_by('id')

    return render(request, 'POS/type_list.html', context={

        'po_type': po_type
    })
@login_required
@permission_required('POS.change_product_type')
def type_edit(request, type_id):
    
    """ แก้ไขประเภท """

    try:
        product_type = Product_type.objects.get(pk=type_id)
        msg = ''
    except Product_type.DoesNotExist:
        return redirect('management')
    
    if request.method == 'POST':
        product_type.name = request.POST.get('name')
        product_type.description = request.POST.get('description')
        product_type.save()
        msg = 'แก้ไขสินค้าสำเร็จแล้ว: %s' %(product_type.name)
    
    context = {
        'po_type': product_type,
        'msg': msg
    }

    return render(request, 'POS/add_type.html', context=context)

@login_required
def type_delete(request, type_id):

    """ สำหรับลบประเภทในดาต้าเบส """
    product_type = Product_type.objects.get(pk=type_id)
    product_type.delete()

    return redirect(to='management')



def report(request):

    search_report = request.GET.get('search_report', '')

    return render(request, 'POS/report.html', context={
        'search_report': search_report,
    })




def show_error_404(request):
    foo = False

    if foo:
        return HttpResponseNotFound('<h1>Not found page.</h1>')
    else:
        return redirect(to='index_home')



# def report(request):

    

#     order = Order.objects.filter(date_time)


def cart(request):
    
    """ ตะกร้า """

    order = Order.objects.all()
    order_product = Order_Products.objects.all()

    return render(request, 'POS/index.html', context={
        'order': order,
        'order_product': order_product,
    })



def add_to_cart(request, product_id):

    product = Product.objects.get(pk=product_id)
    order_product = Order_Products.objects.all()

    if request.method == 'POST':
        order = Order_Products.objects.create(
            product_id=request.POST.get('product_id'),
            description=request.POST.get('description')
        )
    else:
        Type = Product_type.objects.none()

    context = {
        'product_type': Type,
    }

    return render(request, 'POS/index.html', context=context)
