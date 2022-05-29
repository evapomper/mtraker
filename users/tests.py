from django.test import TestCase

from .models import CustomUser


class CustomUserTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = CustomUser.objects.create_user(
            username='testuser1', password='abcd1234', first_name='Eva', last_name='Pomper', gender='Female', phone_number='+79001000000')
        testuser1.save()

        
    def test_customuser_content(self):
        customuser = CustomUser.objects.get(id=1)
        username = f'{customuser.username}'
        first_name = f'{customuser.first_name}'
        last_name = f'{customuser.last_name}'
        gender = f'{customuser.gender}'
        phone_number = f'{customuser.phone_number}'

        self.assertEqual(username, 'testuser1')
        self.assertEqual(first_name, 'Eva')
        self.assertEqual(last_name, 'Pomper')
        self.assertEqual(gender, 'Female')
        self.assertEqual(phone_number, '+79001000000')
