from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryText = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.categoryText}"
    
class Bid(models.Model):
    bid = models.FloatField(blank=True, default=0.0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidOwner", default=None)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid", default=None)   

# class Image(models.Model):
#     name = models.CharField(max_length=50)
#     listing_img = models.ImageField(upload_to='images/', blank=True, null=True)

class Listing(models.Model):
    listingTitle = models.CharField(max_length=80)
    # blank = true means that an entry can be empty in the database
    description = models.CharField(blank=True, max_length=400)
    currentBid = models.FloatField(blank=True, default='0.01')
    isActive = models.BooleanField(default=True, blank=True)
    listingOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myListing", default=None, null=True)
    # destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    imageUrl = models.CharField(max_length=150, blank=True)
    # image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="image", null=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing", default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_listing", null=True)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="listing_bid", null=True)   
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.listingTitle} {self.description} {self.currentBid}"

class Comment(models.Model):
    content = models.CharField(blank=True, max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", default=None)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment", default=None)



