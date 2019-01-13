from django.contrib import admin

from .models import Product

# username: admin, password: password -- I know it's simple, but since this is just a challenge I figured I'll keep it so.
admin.site.register(Product)