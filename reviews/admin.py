''' Register ProductReview on admin '''

from django.contrib import admin
from .models import ProductReview


class ReviewAdmin(admin.ModelAdmin):
    ''' Show product, user, rating on admin panel '''
    list_display = (
        'product',
        'user',
        'rating'
    )


admin.site.register(ProductReview, ReviewAdmin)
