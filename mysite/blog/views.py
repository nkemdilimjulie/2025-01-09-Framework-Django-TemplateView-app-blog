
# # Create your views here.
# from django.http import HttpResponse

# # A view for the homepage or blog index
# def home(request):
#     '''Responds to a request for the blog homepage and returns a simple text message.'''
#     return render(request, 'home.html')
#     return HttpResponse("A Warm Welcome to my Blog Homepage")

# # A view for a specific blog post detail
# def about(request):
#     '''Responds to a request for viewing a specific blog post and accepts an argument (post_id) to identify the post.'''
#     #return HttpResponse(request, 'about.html')
#     return render(request, 'about.html')

from django.views.generic import TemplateView  # new


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
