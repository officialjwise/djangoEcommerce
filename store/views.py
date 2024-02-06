from django.shortcuts import render
from store.models import (
    Category,
    # Tags,
    Vendor,
    Product,
    ProductImages,
    CartOrder,
    CartOrderItems,
    ProductReview,
    Wishlist,
    Address,
)


def index(request):
    product = Product.objects.all().order_by("-id")

    context = {
        "products" : product
    }
    return render(request, 'store/index.html', context)
