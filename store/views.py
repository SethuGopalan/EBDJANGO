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
    