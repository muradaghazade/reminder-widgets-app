# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Widget
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm


class IndexView(ListView):
    model = Widget
    context_object_name = 'widgets'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def payment_process(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100',
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('core:index-page')),
        'return_url': 'http://{}{}'.format(host, reverse('core:index-page')),
        'cancel_return': 'http://{}{}'.format(host, reverse('core:index-page')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment_process.html', {'form': form})