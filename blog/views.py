''' Views to render Blog models '''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Post, Postcategory, Comment
from .forms import PostForm, PostcategoryForm, CommentForm


def all_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()
    postcategories = Postcategory.objects.all()

    if request.GET:
        if 'postcategory' in request.GET:
            postcategories = request.GET['postcategory'].split(',')
            posts = posts.filter(postcategory__name__in=postcategories)
            postcategories = Postcategory.\
                objects.filter(name__in=postcategories)

    context = {
        'posts': posts,
        'postcategories': postcategories,
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, post_id):
    template_name = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

