from django.urls import path
from posts import views

urlpatterns = [ 
    path('', views.get_posts, name='all_posts'),
    path('<int:user_pk>/', views.get_posts, name='my_posts'),
    
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:post_pk>/', views.update_post, name='update_post'),
    path('retrieve_post/<int:post_pk>/', views.retrieve_post, name='retrieve_post'),
    path('delete_post/<int:post_pk>/', views.delete_post, name='delete_post'),
    
]