from django.core.paginator import Paginator
from django.shortcuts import render

import models
from utils import get_page_range


def index_view(request, category_name=None):
    context = {}
    category = None
    if category_name:
        category = models.Category.objects.filter(name__iexact=category_name).first()
        context.update({
            'category': category
        })
    blog_posts = category.blogpost_set.all() if category else models.BlogPost.objects.all()
    paginator = Paginator(blog_posts, 5)
    page = int(request.GET.get('page') or 1)
    context.update({
        'blog_posts': paginator.page(page),
        'page_range': get_page_range(page, paginator.num_pages),
        'categories': models.Category.objects.all()
    })
    return render(request, 'blog/pages/index.html', context=context)


def category_view(request, category_name):
    return index_view(request, category_name)


def blog_post_view(request, blog_post_id):
    blog_post = models.BlogPost.objects.get(id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/pages/blog_post_page.html', context=context)


def notification_preview(request, blog_post_id):
    context = {
        'blog_post': models.BlogPost.objects.get(id=blog_post_id)
    }
    return render(request, 'blog/mailer/publication_notification.html', context=context)
