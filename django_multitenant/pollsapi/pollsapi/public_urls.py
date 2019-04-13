from django.urls import include, path
from tenants.views import TenantsHome


urlpatterns = [
    path('', TenantsHome.as_view(), name='home'),

]