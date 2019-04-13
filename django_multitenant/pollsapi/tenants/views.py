from django.views.generic import TemplateView
from .models import Tenant


class TenantsHome(TemplateView):
    template_name = 'tenants/tenants_home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['tenants'] = Tenant.objects.exclude(schema_name='public')
        return context