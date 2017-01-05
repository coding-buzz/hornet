from django.conf import settings


def google_analytics(request):
    return {'ENABLE_GOOGLE_ANALYTICS': settings.ENABLE_GOOGLE_ANALYTICS}
