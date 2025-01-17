from django.urls import path
from . import views
from myitemapp.views import ItemListView

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),  # myitem homepage
    path("about/", views.AboutPageView.as_view(), name="about"),  # myitemapp detail
    path("item_list/", views.ItemListView.as_view(), name="item_list"),
]
