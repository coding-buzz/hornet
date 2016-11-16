from django.conf import settings


def base_url(request):
    return { 'BASE_URL': settings.BASE_URL }


def mailchimp(request):
    return { 'MAILCHIMP_SUBSCRIPTION_FORM_URL': settings.MAILCHIMP_SUBSCRIPTION_FORM_URL }
