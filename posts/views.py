from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def get_posts(request):
    """
    this creates a View which returns a List of Posts that were 
    published prior to 'now' and will render them
    to the "blogposts.html" template 
    """
    
    # __lte= means 'less than or equal to'
    posts = Post.Object.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, "blogposts.html", {'posts': posts})
    
    
    
    
def post_detail(request, pk):
    """
    this creates a View which returns a single Post object based on the post ID (pk)
    and will render it to the "postdetail.html" template.
    Or return a 404 error, if post not found.
    """
    
    post = get_object_or_404(Post, pk=pk)
    post.views +=1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def create_or_edit_post(request, pk=None):
    """
    this creates a View which allows us to edit or create a post depending
    if the post ID is null or not
    """
    
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method== "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})