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
    # product = Product.objects.all().order_by("-id")
    product = Product.objects.filter(product_status="published", featured=True).order_by("-id")
    context = {
        "products": product
    }
    return render(request, 'store/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'store/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'store/category-list.html', context)
