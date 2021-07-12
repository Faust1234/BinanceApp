from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
# Create your views here.
# def index(request):
#
#     list_articles = Articles.objects.all()
#
#     context = {
#         'list_articles': list_articles
#     }
#     template = 'binance/index.html'
#     return render(request, template, context)


class HomeListView(ListView):
    model = Articles
    template_name = 'binance/index.html'
    context_object_name = 'list_articles'


# def information_page(request, id):
#     get_article = Articles.objects.get(id=id)
#     context = {
#             'get_article':get_article
#     }
#
#     template = 'binance/information.html'
#
#     return render(request, template, context)



class HomeDetailView(DetailView):
    model = Articles
    template_name = 'binance/information.html'
    context_object_name = 'get_article'

def edit_page(request):
    context = {
            }
    template = 'binance/edit_page.html'
    return render(request, template, context)






