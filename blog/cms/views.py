from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Blog_post
from forms import Blog_postForm

def homepage(request):
    post_list = Blog_post.objects.order_by('-date')[:10]
    return render(request, 'blog/index.html', {'posts': post_list})

def new_post(request):
    if request.method == 'POST':
        form = Blog_postForm(data=request.POST)
        if form.is_valid():
            blog_post = form.save()
            return HttpResponseRedirect('/blog/page/%s'% blog_post.title_slug)
        else:
            print form.errors()
    else:
        form = Blog_postForm()
    return render(request, 'blog/new_page.html', {'form':form})

def view_post(request, blog_post_slug):
    context_dict = {}
    try:
        post = Blog_post.objects.get(title_slug=blog_post_slug)
        context_dict['content'] = post.post_text
        context_dict['title'] = post.title
        context_dict['date'] = post.date.date
    except Blog_post.DoesNotExist:
        # If the post doesn't exist just return the slug as a title
        # Display a default template
        context_dict['title'] = blog_post_slug
    return render(request, 'blog/blog_page.html', context_dict)
