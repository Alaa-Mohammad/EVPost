from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from posts.models import Post, PostGallery
from django.contrib.auth.decorators import login_required

# Get posts for all users or logged in user
def get_posts(request, user_pk=None):
    if user_pk != None:
        user = get_object_or_404(User, pk=user_pk)
        data = Post.objects.select_related('user').filter(user= user, is_available=True)
        
    else:
        data = Post.objects.select_related('user').filter(is_available=True)
        
    paginator = Paginator(data,6)
    page_number = request.GET.get('page')
    post_count = data.count()
    
    try:
        paged_posts = paginator.get_page(page_number)  
    except PageNotAnInteger:
        paged_posts = paginator.page(1)
    except EmptyPage:
        paged_posts = paginator.page(paginator.num_pages)

    context = {
        'posts': paged_posts,
        'post_count':post_count,
             }
    
    return render(request, 'post/get_posts.html', context)


@login_required(login_url = 'login')
def create_post(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        content= request.POST.get('content')
        images= request.FILES.getlist('images')    
        
        post= Post.objects.create(user=request.user,title= title, content= content )
        if images:
            for item in images:
                if 'image' in item.content_type :
                    obj= PostGallery.objects.create(post=post,image=item)

        return redirect(reverse('my_posts',args=(request.user.id,)))
    else:
        return render(request, 'post/create_post.html')


def retrieve_post(request,post_pk):
    post= get_object_or_404(Post, pk=post_pk, is_available=True )
    return render(request, 'post/retrieve_post.html',context={'post':post})


@login_required(login_url = 'login')
def update_post(request,post_pk):
    if request.method=='POST':
        post= get_object_or_404(Post, pk=post_pk, is_available=True)
        if post.user == request.user:
            title= request.POST.get('title')
            content= request.POST.get('content')
            deleted_images= request.POST.getlist('deleted_imgs')
            added_images= request.FILES.getlist('images')

            for item in added_images:
                PostGallery.objects.create(post=post,image=item)
            
            for image_id in deleted_images:
                if image_id != 'no_data':
                   PostGallery.objects.get(id=int(image_id),post=post).delete()
                
        return redirect(reverse('retrieve_post',args=(post.id,)))
    else:
        post= get_object_or_404(Post, pk=post_pk, is_available=True)
        
        return render(request, 'post/update_post.html',{'post':post})


@login_required(login_url = 'login')
def delete_post(request, post_pk):
    post= get_object_or_404(Post, pk=post_pk, is_available=True)
    post.is_available=False
    post.save()
    return redirect(reverse('my_posts',args=(request.user.id,)))
    