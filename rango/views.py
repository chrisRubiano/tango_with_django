from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
from rango.models import Page, Category
from rango.forms import PageForm, CategoryForm
# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')
    pages_list = Page.objects.order_by('views')
    most_viewed_pages_list = Page.objects.order_by('-views')[:5]
    # for category in category_list:
    #     for page in pages_list:
    #         if category.name == page.category.name:
    #             print(page.category.name)
    context_dict = {'categories': category_list, 'pages': pages_list, 'most_viewed': most_viewed_pages_list}
    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_url):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_url)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()

    #a http post?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
            else:
                print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)



