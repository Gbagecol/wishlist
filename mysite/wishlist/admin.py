from .models import User, Wishlist, WishlistEntry
from django.contrib import admin


admin.site.register(User)
admin.site.register(Wishlist)
admin.site.register(WishlistEntry)