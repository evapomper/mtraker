from django.test import TestCase

from users.models import CustomUser
from .models import Category, SubCategory, Item, Purchase


class PurchaseTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = CustomUser.objects.create_user(
            username='testuser1', password='abcd1234', first_name='Eva', last_name='Pomper', gender='Female', phone_number='+79001000000')
        testuser1.save()

        category1 = Category.objects.create(name='Food')
        category1.save()

        subcategory1 = SubCategory.objects.create(
            name='Meat', category=category1)
        subcategory1.save()

        item1 = Item.objects.create(
            name='Beef on the bone', subcategory=subcategory1, ean=123456)
        item1.save()

        purchase1 = Purchase.objects.create(
            username=testuser1, item=item1, price=400, amount=1)
        purchase1.save()

    def test_purchase_content(self):
        purchase = Purchase.objects.get(id=1)
        username = f'{purchase.username}'
        item = f'{purchase.item}'
        price = f'{purchase.price}'
        amount = f'{purchase.amount}'

        self.assertEqual(username, 'testuser1')
        self.assertEqual(item, 'Beef on the bone')
        self.assertEqual(price, '400')
        self.assertEqual(amount, '1')



