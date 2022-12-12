import datetime

from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['carousels'] = Carousel.objects.all()
        self.views['offers'] = Offer.objects.all()
        self.views['vendors'] = Vendor.objects.all()
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['hots'] = Product.objects.filter(labels='hot')
        self.views['sales'] = Product.objects.filter(labels='sale')
        return render(request, 'index.html', self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        self.views
        ids = Category.objects.get(slug=slug).id
        self.views['catproducts'] = Product.objects.filter(category_id=ids)
        return render(request, 'category.html', self.views)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views
        self.views['productdetails'] = Product.objects.filter(slug=slug)
        subcat_ids = Product.objects.get(slug=slug).subcategory_id
        self.views['related_products'] = Product.objects.filter(subcategory_id=subcat_ids)
        self.views['product_reviews'] = Product.objects.filter(slug=slug)
        return render(request, 'detail.html')

def product_review(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        slug = request.POST['slug']
        review = request.POST['review']
        star = request.POST['star']
        x = datetime.datetime.now()
        date = x.strftime("%c")

        data = ProductReview.objects.create(
            name = name,
            email = email,
            slug = slug,
            review = review,
            star = star,
            date = datetime
        )
        data.save()
        return redirect(f'/product_details/{slug}')