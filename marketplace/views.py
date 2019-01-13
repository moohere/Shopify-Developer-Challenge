from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages

# The index view is simply the homepage of the marketplace. There are two context written right away, one to showcase all products,
# and one to showcase all products that have at least 1 inventory. By default, we view all available products. 
def index(request):
    product_list_all = Product.objects.all()
    product_list = Product.objects.exclude(inventory_count = 0)
    # When you click on Show One button, you can view every product including those with 0 inventory through a drop down list.
    if "showOne" in request.POST:
        product = Product.objects.all()[:1].get()
        return render(request, 'marketplace/single.html', {'product':product, 'product_list_all': product_list_all})
    # When you click on Show All button, you can view every available product, redirects you to the homepage.
    if "showAll" in request.POST:
        return render(request, 'marketplace/index.html', {'product_list' : product_list,})
    # Tried to do everything using only 2 views here so I put the View Product button to direct you to the single.html template.
    # This is where you can view each product description individually and click on More Details to go to the purchase page.
    if "showProduct" in request.POST:
        product_id = request.POST["products"]
        product = get_object_or_404(Product, pk = int(product_id))
        return render(request, 'marketplace/single.html', {'product': product, 'product_list_all': product_list_all})
    return render(request, 'marketplace/index.html', {'product_list':product_list,})

def detail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    context = {'product': product}
    # If Purchase button is clicked, and there is inventory, it will reduce the inventory count and send the user a message
    # confirming that the product has been purchased. The updated inventory is immediately shown. 
    if "purchase" in request.POST:
        if product.inventory_count >= 1:
            product.inventory_count -= 1
            product.save()
            product_list = Product.objects.exclude(inventory_count = 0)
            messages.info(request, "You have successfully purchased a %s" % product.title)
            return render(request, 'marketplace/detail.html', context)
        else:
            messages.info(request, "%s is sold out!" % product.title)
            return render(request, 'marketplace/detail.html', context)
    return render(request, 'marketplace/detail.html', context)