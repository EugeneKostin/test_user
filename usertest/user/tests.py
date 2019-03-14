from django.test import TestCase, Client
from .models import User
from .views import UserRegistrationForm
from .forms import *
from django.urls import reverse
from . import urls
# Create your tests here.
class TestUserRegistration(TestCase): 
  
  def setUp(self):
    self.client = Client()
    User.objects.create(email = 'zh.kostin@mail.ru', password = '123123', username = 'zh.kostin', second_name = 'Eugene', first_name = 'Kostin', last_name = 'Vladimirovich', birth_date = '1997-08-21', auth_key = '11111')
    self.url = reverse('registration')
  
  def test_age(self):
    user = User.objects.get(username = 'zh.kostin')
    self.assertEqual(user.calculate_age(), 21)
  
  def test_registration_template(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    
  def test_user_creation(self):
    self.client.post(self.url, data={'email': 'test_user@mail.ru', 'password1': '59351089Zzz', 'password2': '59351089Zzz', 'username': 'user', 'second_name': 'userok', 'first_name': 'userov', 'last_name': 'useerovich', 'birth_date': '1997-08-21', 'auth_key': '2222'})
    self.assertEqual(User.objects.count(), 2)
  
  def test_registration(self):
    wrong = self.client.post(self.url, data={'email': 'test_user1@mail.ru', 'password1': '59351089Zz', 'password2': '59351089Zzz', 'username': 'user1', 'second_name': 'userok', 'first_name': 'userov', 'last_name': 'useerovich', 'birth_date': '1997-08-21', 'auth_key': '2222'})
    wrong = self.client.post(self.url, data={'email': 'test_user3', 'password1': '59351089Zzz', 'password2': '59351089Zzz', 'username': 'user3'})
    corr = self.client.post(self.url, data={'email': 'test_user2@mail.ru ', 'password1': '59351089Zzz', 'password2': '59351089Zzz', 'username': 'user2'})
    user = User.objects.get(username = 'user2')
    self.assertEqual(user.email, 'test_user2@mail.ru')

class LoginTest(TestCase):
    def setUp(self):
        User.objects.create_user(email = 'zh.kostin@mail.ru', password = '123123', username = 'zh.kostin', second_name = 'Eugene', first_name = 'Kostin', last_name = 'Vladimirovich', birth_date = '1997-08-21', auth_key = '11111')
        self.url = reverse('login')
   
    def test_login(self):
        response = self.client.post(self.url, data={'username': '  zh.kostin ', 'password': '123123 '}, follow=True)
        self.assertTrue(response.context['user'].is_active)

class EditFormTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(email = 'zh.kostin@mail.ru', password = '123123', username = 'zh.kostin', second_name = 'Eugene', first_name = 'Kostin', last_name = 'Vladimirovich', birth_date = '1997-08-21', auth_key = '11111')
        response = self.client.post(self.url, data={'username': '  zh.kostin ', 'password': '123123 '}, follow=True)

    def test_edit_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_validate_input(self):

        form = UserChangeForm({
            'email' : "zh.kostin1997@gmail.com",  
            'username' : "zh.kostin123", 
            'second_name' : "testsecond", 
            'first_name' : "testfirst", 
            'last_name' : "testlast", 
            'birth_date' : "1997-08-21", 
            'auth_key' : "131231"
        }, instance = self.user)
        
        self.assertTrue(form.is_valid())

        edit_user = form.save()

        self.assertEqual(form.cleaned_data['email'], 'zh.kostin1997@gmail.com')
        self.assertEqual(form.cleaned_data['username'], 'zh.kostin123')
        self.assertEqual(form.cleaned_data['second_name'], 'testsecond')
        self.assertEqual(form.cleaned_data['auth_key'], '131231')
                
        self.assertEqual(edit_user.email, "zh.kostin1997@gmail.com")
        self.assertEqual(edit_user.first_name, "testfirst")
