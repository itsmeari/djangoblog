from django.contrib import admin
from .models import Post, Category, Comment

class blog_admin(admin.ModelAdmin):
	list_display = ("title", "pub_date", "was_published_recently")
	search_fields = ["title"]

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
