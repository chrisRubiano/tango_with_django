from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
from rango.models import Category
from rango.models import Page
# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('views')
    # for category in category_list:
    #     for page in pages_list:
    #         if category.name == page.category.name:
    #             print(page.category.name)
    context_dict = {'categories': category_list, 'pages': pages_list}
    return render(request, 'rango/index.html', context=context_dict)
