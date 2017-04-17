from django.views.generic.base import TemplateView


class DashboardView(TemplateView):

    template_name = 'pinger/pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = {}
        return context
