from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
 
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post, 'posts' : posts})

def delete_post(request, id):
	#check they have admin ability
    if request.user.is_superuser:
        Post.objects.get(id=id).delete()
    return HttpResponseRedirect("/")
