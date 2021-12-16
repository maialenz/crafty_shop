''' Views to render Review model to template '''
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import ProductReview


@login_required
def add_review(request, product_id):
    ''' Get product object and create review '''
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating', '')
        content = request.POST.get('content', '')
        review = ProductReview.objects.create(
            product=product, user=request.user, rating=rating, content=content)

        messages.success(request, 'Thanks! Your review was added!')

        return redirect(reverse('product_detail', args=[product.id]))

    else:
        messages.error(request, 'Sorry an error has occurred. Please \
            try again.')

        return redirect(reverse('product_detail', args=[product.id]))
