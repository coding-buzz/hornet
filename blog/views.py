from django.core.paginator import Paginator
from django.shortcuts import render, redirect

import models
import forms
from utils import get_page_range


def index_view(request, category_name=None):
    context = {}
    category = None
    if category_name:
        category = models.Category.objects.filter(name__iexact=category_name).first()
        context.update({
            'category': category
        })
    blog_posts = (category.blogpost_set if category else models.BlogPost.objects).exclude(published_at__isnull=True)
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


def blog_post_view(request, blog_post_id, comment_form=None):
    blog_post = models.BlogPost.objects.get(id=blog_post_id)
    if blog_post.published_at is None and blog_post.preview_key != request.GET.get('preview_key', ''):
        return redirect('blog:index')
    context = {
        'blog_post': blog_post,
        'comment_form': comment_form or forms.CommentForm(),
    }
    if comment_form:
        context.update({
            'anchor': 'comments-section'
        })
    return render(request, 'blog/pages/blog_post_page.html', context=context)


def notification_preview(request, blog_post_id):
    context = {
        'blog_post': models.BlogPost.objects.get(id=blog_post_id)
    }
    return render(request, 'blog/mailer/publication_notification.html', context=context)


def add_comment(request, blog_post_id):
    form = forms.CommentForm(request.POST)
    if form.is_valid():
        form.instance.blog_post = models.BlogPost.objects.get(id=blog_post_id)
        form.save()
        response = redirect('blog:blog_post_view', blog_post_id=blog_post_id)
        response['Location'] += '#{}'.format(form.instance.get_anchor_name())
        return response
    return blog_post_view(request, blog_post_id, comment_form=form)
