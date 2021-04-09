# Predefined packages
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib import messages

# Custom packages
from product.models import Order

# Create your views here.
class HomeListView(ListView):
    model = Order

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            orders = Order.objects.filter(user = self.request.user)
            context = dict()

            context = {
                'orders': orders
            }
            return render(self.request, 'core/home.html', context)
        else:
            return render(self.request, 'core/home.html')