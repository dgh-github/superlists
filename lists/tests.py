from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

  def test_root_url_resolve_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func,home_page)

  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    html = response.content.decode('utf-8')
    self.assertTrue(html.startswith('<html>'))
    self.assertIn('<title>待办事项清单</title>', html)
    self.assertTrue(html.strip().endswith('</html>'))
    self.assertTemplateUsed(response, 'home.html')
    
