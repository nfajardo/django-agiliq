from django.views.generic import ListView

from .models import Category, Origin

# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = 'entities/categories.html'


class OriginListView(ListView):
    model = Origin
    template_name = 'entities/origin.html'    