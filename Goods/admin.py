from django.contrib import admin

# Register your models here.
from Goods.models import User, Goods, Banner

admin.site.register(User)
admin.site.register(Goods)
admin.site.register(Banner)
