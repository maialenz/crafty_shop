from django.shortcuts import render, reverse, get_object_or_404

from .models import BlogPost


def all_blog_posts(request):
    """
    View all blog posts on template 
    """
    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)