from django.contrib import admin
from .models import Product, Article, Tag, Room, Message

# Register your models here.

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Room)
admin.site.register(Message)