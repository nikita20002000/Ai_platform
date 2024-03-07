from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sell
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum

class SellsList(LoginRequiredMixin, ListView):
    model = Sell
    template_name = 'sells/sells_list.html'

    context_object_name = 'sells'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sells'] = context['sells'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['sells'] = context['sells'].filter(
                name__icontains=search_input,)

        context['search-input'] = search_input

        return context



class SellDetail(DetailView):
    model = Sell
    template_name = 'sells/sell.html'

    context_object_name = 'sell'


class SellCreate(LoginRequiredMixin, CreateView):
    model =Sell

    template_name = 'sells/sell_form.html'

    fields = [
        'date',
        'summ',
        'name',
        'category',
        'amount',
        'price_for_one',
        'full_price',
        'margue',
        'status',
    ]

    success_url = reverse_lazy('sells:sells-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SellCreate, self).form_valid(form)


class SellUpdate(UpdateView):
    model = Sell

    template_name = 'sells/sell_form.html'

    fields = [
        'date',
        'summ',
        'name',
        'category',
        'amount',
        'price_for_one',
        'full_price',
        'margue',
        'status',
    ]

    success_url = reverse_lazy('sells:sells-list')


class DeleteSell(DeleteView):
    model = Sell
    context_object_name = 'sell'

    success_url = reverse_lazy('sells:sells-list')


class SellVisualization(LoginRequiredMixin, ListView):
    model = Sell

    template_name = 'visualization/visualization_dashboard.html'



    context_object_name = 'sells'

    def get_context_data(self, **kwargs):
        from datetime import date
        context = super().get_context_data(**kwargs)

        context['sells'] = context['sells'].filter(user=self.request.user)

        # СБОР ДАННЫХ ПО КАТЕГОРИЯМ И СУММЕ
        mid_dict ={}
        for i in context['sells']:
            mid_dict[i.category] = mid_dict.get(i.category, 0) + i.summ

        context['sells']

        # СБОР ДАННЫХ ПО НАЗВАНИЮ И ОБЩЕЙ СУММЕ
        mid_dict_2 = {}
        for j in context['sells']:
            mid_dict_2[j.name] = mid_dict_2.get(j.name, 0) + j.summ

        # CБОР ДАННЫХ ПО СТАТУСУ ОПЛАТЫ
        mid_dict_3 = {}
        for k in context['sells']:
            mid_dict_3[k.status] = mid_dict_3.get(j.status, 0) + 1

        # СБОР ДАННЫЗ ПО КОЛИЧЕСТВО ПРОДАННЫХ ЕДИНИЦ
        my_dict_4 = {}
        for l in context['sells']:
            my_dict_4[l.name] = my_dict_4.get(l.name, 0) + l.amount

        # СБОР ДАННЫХ ПО ДАТАМ И ОБЩЕЙ СУММЕ
        mid_dict_5 = {}
        for d in context['sells']:
            mid_dict_5[d.date] = mid_dict_5.get(d.date, 0) + d.summ



        context = {
            'categories_max': [[key, value] for key, value in mid_dict.items()],
            'by_name_max': [[key, value] for key, value in mid_dict_2.items()],
            'sort_by_order': [[key, value] for key,value in mid_dict_3.items()],
            'sort_by_amount': [[key, value] for key, value in my_dict_4.items()],
            'sort_by_date': [[key, value] for key, value in mid_dict_5.items()],
            'sells': context
        }



        return context