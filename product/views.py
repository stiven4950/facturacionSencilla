# predefined packages
import random
import string


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic.list import View
from django.views.generic.detail import DetailView

from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required

# custom packages
from .models import Item, Order
from registration.models import Profile

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

# Create your views here.
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        total_price = 0
        items = Item.objects.filter(user = self.request.user, ordered=False)
        context = {}

        if len(items) <= 0:
            messages.info(self.request, "No tienes productos registrados aún.")
        else:
            for item in items:
                total_price += item.get_total_item_price()
            context = {
                'total': total_price,
                'items': items
            }

        return render(self.request, 'product/product_list.html', context)

def add_product(request):
    json_response = {'created': False}
    if request.user.is_authenticated:
        nameR = request.GET.get('name', None)
        priceR = request.GET.get('price', None)
        quantityR = request.GET.get('quantity', None)

        if nameR != "" and priceR != "" and quantityR != 0:
            Item.objects.create(
                name=nameR,
                price=priceR,
                quantity= quantityR,
                user=request.user)
            json_response['created'] = True
            messages.success(request, "Registrado con éxito :)")
    else:
        print("La verga")
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

@login_required
def remove_product(request, pk):
    item = Item.objects.filter(user=request.user, pk=pk)
    if item.exists():
        item.delete()
        messages.info(request, "Producto Eliminado")
        return redirect("product:order")
    else:
        messages.info(request, "No se encontró el producto")
        return redirect("product:order")

@login_required
def remove_one_product(request, pk):
    item = Item.objects.filter(user=request.user, pk=pk)

    if item.exists():
        item_a = item[0]
        if item_a.quantity > 1:
            item_a.quantity -= 1
            item_a.save()
            messages.info(request, "La cantidad fue actualizada")
            return redirect("product:order")
        else:
            remove_product(request, pk)
    else:
        messages.info(request, "No se encontró el producto")
        return redirect("product:order")

@login_required
def add_one_product(request, pk):
    item = Item.objects.filter(user=request.user, pk=pk)

    if item.exists():
        item_a = item[0]

        item_a.quantity += 1
        item_a.save()
        messages.info(request, "La cantidad fue actualizada")
        return redirect("product:order")
    else:
        messages.info(request, "No se encontró el producto")
        return redirect("product:order")

@login_required
def generate_order(request):
    global_price = 0
    items = Item.objects.filter(user = request.user, ordered=False)

    if items.exists():
        order = Order.objects.create(user=request.user)

        order.ref_code = create_ref_code()
        
        for item in items:
            order.items.add(item)
            global_price += item.get_total_item_price()
            item.ordered = True
            item.save()
        
        order.global_price = global_price
        order.save()
        
        return redirect("product:orderdetail", order.pk)
    else:
        messages.warning(request, "No se logró ejecutar la operación")
        return redirect("product:order")

class OrderDetailView(DetailView):
    def get(self, *args, **kwargs):
        order = Order.objects.filter(user = self.request.user, pk=self.kwargs['pk'])
        profile_user = Profile.objects.get(user = self.request.user)

        context = {}

        if order.exists():
            context = {
                'order':order[0],
                'user':profile_user
            }
            return render(self.request, 'product/order_detail.html', context)
        else:
            return render(self.request, 'product/order_detail.html')