from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=100)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Carousel(models.Model):
      name = models.CharField(max_length=500)
      image = models.ImageField(upload_to='media')
      url = models.URLField(max_length=500)
      description = models.TextField(blank=True)

      def __str__(self):
          return self.name

class Feature(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=100)
    slug = models.CharField(max_length=500, unique=True)


class Offer(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField(unique=True)
    slug = models.CharField(max_length=500, unique=True)

LABELS = (('new','New'),('hot','Hot'),('sale','Sale'),('','Default'))
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    labels = models.CharField(choices=LABELS, max_length=50)
    stock = models.CharField(choices=STOCK, max_length=50)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    review = models.TextField()
    date = models.CharField(max_length=50)
    slug = models.CharField(max_length=500)
    star = models.IntegerField(default=1)

    def __str__(self):
        return self.name
