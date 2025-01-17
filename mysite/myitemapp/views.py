from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Item

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class ItemListView(ListView):
    template_name = "item_list.html"
    # def item_list(request):
    #     # Retrieve all Item objects from the database
    #     items = Item.objects.all()
    #     return render(request, "myitemapp/item_list.html", {"items": items})
