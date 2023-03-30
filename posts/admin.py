from django.contrib import admin
from posts.models import Post, Review
#Register your models here.

admin.site.register(Post)
admin.site.register(Review)