from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),  # Blog homepage
    path("about/", views.AboutPageView.as_view(), name="about"),  # Blog detail
]


# Resulting URL Paths
# URL	                            Handled By	                    View Function
# http://127.0.0.1:8000/	        path("", views.home_view)	    home_view
# http://127.0.0.1:8000/about/	    path("about/", ...)	            about_view
# http://127.0.0.1:8000/contact/	path("contact/", ...)	        contact_view
# 
