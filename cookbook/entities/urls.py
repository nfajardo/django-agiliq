from django.urls import path

from .views import CategoryListView, OriginListView

app_name = "entities"
urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("origin/", OriginListView.as_view(), name="origin"),
]
