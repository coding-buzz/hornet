from django.views.generic.base import TemplateView

import pinger.models as models


class DashboardView(TemplateView):

    template_name = 'pinger/pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = {
            'ping_checks': models.PingCheck.objects.all(),
            'response_checks': models.ResponseCheck.objects.all(),
        }
        return context
