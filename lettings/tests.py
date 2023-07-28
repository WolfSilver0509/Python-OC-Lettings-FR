from django.test import TestCase
from django.urls import reverse

class LettingsTestCase(TestCase):

    fixtures = ['lettings.json']
    def test_lettings_index(self):
        """ Test pour la page d'accueil """
        url = reverse('lettings_index')
        response = self.client.get(url)
        html_content = response.content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lettings", html_content)

    def test_lettings(self):
        """ Test pour la page de lettings """
        url = reverse('letting', kwargs={'letting_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
