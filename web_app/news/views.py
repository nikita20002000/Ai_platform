from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from news.scripts.news_parser import get_news

def news_list(request):
    topic_theme = request.POST.get('topic_theme', 'Business')
    news = get_news(keyword=topic_theme)

    return render(request, 'news_list/news_list.html', context=news)

def get_news_with_topic(request):
    topic_theme = request.POST.get('topic_theme', 'undefined')

    print(topic_theme)
    news = get_news(keyword="topic_theme")
    return render(request, 'news_list/news_list.html', context=news)