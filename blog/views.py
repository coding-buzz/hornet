from django.shortcuts import render


def index_view(request):
    return render(request, 'blog/pages/index.html')
