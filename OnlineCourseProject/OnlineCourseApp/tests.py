from django.test import TestCase
from .models import Category


class ItemModelTest(TestCase):
    def test_save_and_retrieve(self):
        item1 = Category(categoryId='11', title='computer science')
        item1.save()
        item2 = Category(categoryId='12', title='marketing')
        item2.save()
        saved_items = Category.objects.all()
        self.assertEqual(saved_items.count(), 2)
        saved_item1 = saved_items[0]
        saved_item2 = saved_items[1]
        self.assertEqual(item1.categoryId, '11')
        self.assertEqual(item2.categoryId, '12')
