from django.shortcuts import render
from .models import Posts, Categories , SubCategories
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse
from django.views.generic.detail import DetailView


class PostDetailView(DetailView):
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ResultPost'] = Posts.objects.filter(
            sub_category=kwargs['object'].sub_category_id)
        return context
    

class PageView(ListView):
    model = Posts  

def subCategoriesData(request):
    Result = Categories.objects.filter(
        parent=request.GET['categoryid']).values()
    return JsonResponse({"sub_categories_data": list(Result)})
