from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Post


class PostTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.post = Post.objects.create(title='First', text="this is test text")
	
	def test_model_content(self):
		self.assertEqual(self.post.text, 'this is test text')
		self.assertEqual(self.post.title, 'First')
	
	def test_url_at_correct_location(self):
		response = self.client.get('/')
		print(response)
		self.assertEqual(response.status_code, 200)
	
	def test_home_page(self):
		response = self.client.get(reverse('home_page'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'base.html')
		self.assertContains(response, 'this is test text')

	
