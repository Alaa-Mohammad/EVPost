from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=20)
    content= models.TextField()
    is_available= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('retrieve_post', args=(self.id,))
                        
        
    def __str__(self):
        return self.user.username


class PostGallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/posts/%y/%m/%d/', max_length=255)

    def __str__(self):
        return self.post.user.username

    class Meta:
        verbose_name = 'postgallery'
        verbose_name_plural = 'post gallery'