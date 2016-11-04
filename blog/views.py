from django.shortcuts import render

import models


def index_view(request):
    context = {
        'blog_posts': models.BlogPost.objects.all()
    }
    return render(request, 'blog/pages/index.html', context=context)
