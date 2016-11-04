from django.shortcuts import render

import models


def index_view(request):
    context = {
        'blog_posts': models.BlogPost.objects.all()
    }
    return render(request, 'blog/pages/index.html', context=context)


def blog_post_view(request, blog_post_id):
    blog_post = models.BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/pages/blog_post_page.html', context=context)
