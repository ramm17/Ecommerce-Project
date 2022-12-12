from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Carousel)
admin.site.register(Offer)
admin.site.register(Vendor)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(ProductReview)