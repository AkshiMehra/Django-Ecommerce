from django.shortcuts import redirect, render
from .models import Product
from django.core.paginator import Paginator
from .models import Orders

# Create your views here.


def index(request):
    products = Product.objects.all()
    items = request.GET.get('name_')
    if items != "" and items is not None:
        products = products.filter(prod_name__icontains=items)

    #list of objects, products per page
    pagin = Paginator(products, 4)
    page_no = request.GET.get('page')
    products = pagin.get_page(page_no)
    return render(request, 'Myshop/index.html', {'prod': products, })


def detail(request, id):
    item = Product.objects.get(pk=id)

    return render(request, 'Myshop/details.html', {'item': item, })

def checkout(request):

    if request.method == "POST":

        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        addr = request.POST.get("addr","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip = request.POST.get("zip","")
        items = request.POST.get("items")
        total = request.POST.get("total",0)

        order = Orders(items = items, name = name, address = addr, city = city, state = state, zip = zip, total = total)
        order.save()

        # return redirect('myshop:index')
    return render(request, "Myshop/checkout.html")