from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
import os

from .models import Code
from  .forms import CodeForm


class Home(ListView):
    model = Code
    template_name = 'snippets/index.html'
    context_object_name = 'content'


def languageShow(request, language):
    content = Code.objects.filter(language__icontains=language)
    return render(request, 'snippets/language.html', {'content': content})


class allSnippets(ListView):
    model = Code
    template_name = 'snippets/snippets.html'
    context_object_name = 'content'


class DetailCode(DetailView):
    model = Code
    template_name = 'snippets/detail.html'
    context_object_name = 'content'


def hashtag(request, hashtag_name):
    content = Code.objects.filter(tags__contains=hashtag_name)
    return render(request, 'snippets/hashtag.html', {'content': content})


def updateSnippets(request, snippet_id):

    if request.method == 'POST':
        form = CodeForm(request.POST, instance=snippet_id)
        if form.is_valid():
            code = form.save(commit=False)
            code.title = form.data['title']
            code.save()
            return redirect('/')
    else:
        form = CodeForm()

    return render(request, 'snippets/form.html', {'forms': form})


def new_post(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.url = form.data['title']
            article.save()
            return redirect('/')
    else:
        form = CodeForm()
    return render(request, 'snippets/form.html', {'forms': form})


def search(request):
    if request.method == 'POST':
        search_result = request.POST['searched']
        result = Code.objects.filter(Q(title__icontains=search_result) | Q(tags__icontains=search_result) | Q(text=search_result) | Q(language__icontains=search_result))
        return render(request, 'snippets/search.html', {'content': result})
    else:
        return render(request, 'snippets/search.html')






