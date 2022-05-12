from django.contrib import admin

# Register your models here.
from .models import User, Comment, Bid, Listing, Category

# Register your models here.
admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Category)