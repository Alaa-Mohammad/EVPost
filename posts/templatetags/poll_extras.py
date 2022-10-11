from django import template
from posts.models import PostGallery

register= template.Library()

@register.simple_tag
def get_images(post):
    return PostGallery.objects.filter(post=post)

@register.filter
def to_str(value):
    return str(value)