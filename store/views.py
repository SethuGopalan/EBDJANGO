from django.shortcuts import get_object_or_404, render

"""
to give access to models bring models here
"""

from .models import Product ,Category
"""

application to request all the urls
"""

def all_products(request):

    """
    qury to reqest all the products/running a qurry to product table collecting all the data
    """
    
    products = Product.objects.all()
    """
    loading home template
    """
    
    return render(request, 'store/home.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
    