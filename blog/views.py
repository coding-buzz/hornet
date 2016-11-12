from django.core.paginator import Paginator
from django.shortcuts import render

import models
from utils import get_page_range


def index_view(request):
    blog_posts = models.BlogPost.objects.all()
    paginator = Paginator(blog_posts, 5)
    page = int(request.GET.get('page') or 1)
    context = {
        'blog_posts': paginator.page(page),
        'page_range': get_page_range(page, paginator.num_pages)
    }
    return render(request, 'blog/pages/index.html', context=context)


def blog_post_view(request, blog_post_id):
    blog_post = models.BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/pages/blog_post_page.html', context=context)
