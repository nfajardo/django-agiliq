from django.contrib import admin
from tenants.utils import tenant_from_request

from .models import Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
