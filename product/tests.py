from django.test import TestCase
from django.contrib.auth.models import User

from .models import Order, Item
from .views import create_ref_code


# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.product1 = Item.objects.create(name='Martillo', user=self.user1, price=20000, quantity=5)
        self.product2 = Item.objects.create(name='Alicate', user=self.user1, price=15000, quantity=2)
        
        self.order = Order.objects.create(user=self.user1)
    
    def test_total_price_product(self):
        self.assertEqual(self.product1.get_total_item_price(), 100000.0)
    
    def test_add_products_to_order(self):
        self.order.items.add(self.product1,self.product2)
        self.assertEqual(len(self.order.items.all()), 2)
    
    def test_order_created_global_price(self):
        product3 = Item.objects.create(name='Galletas', user=self.user1, price=1200, quantity=12)
        self.order.items.add(self.product1,self.product2, product3)

        self.order.ref_code = create_ref_code()
        global_price=0
        for item in self.order.items.all():
            global_price += item.get_total_item_price()
            item.ordered = True
            item.save()
        
        self.order.global_price = global_price
        self.order.save()

        self.assertEqual(self.order.global_price, 144400.0)