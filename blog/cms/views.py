from django.shortcuts import render
from models import Blog_post
from cms import markdown

def homepage(request):
    context_dict = {}
    post_list = Blog_post.objects.order_by('-date')[:10]
    return render(request, 'blog/index.html', context_dict)

def new_post(request):
    return render(request, 'blog/new_page.html')

def view_post(request, blog_post_slug):
    context_dict = {}
    try:
        post = Blog_post.objects.get(title_slug=blog_post_slug)
        context_dict['content'] = markdown.parse(post.post_text)
        context_dict['title'] = post.title
    except Blog_post.DoesNotExist:
        # If the post doesn't exist just return the slug as a title
        # Display a default template
        context_dict['title'] = blog_post_slug
    return render(request, 'blog/blog_page.html', context_dict)
