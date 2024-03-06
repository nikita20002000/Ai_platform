from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sell
from django.contrib.auth.mixins import LoginRequiredMixin

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