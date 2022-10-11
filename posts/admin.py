from django.contrib import admin
from .models import Post,  PostGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class PostGalleryInline(admin.TabularInline):
    model = PostGallery
    extra = 1

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_available')
    inlines = [PostGalleryInline]