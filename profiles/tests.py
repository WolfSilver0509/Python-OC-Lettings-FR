from django.test import TestCase
from django.urls import reverse

class ProfilesTestCase(TestCase):

    fixtures = ['auth.json', 'profiles.json']
    def test_profiles_index(self):
        """ Test pour la page d'accueil """
        url = reverse('profiles_index')
        response = self.client.get(url)
        html_content = response.content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Profiles", html_content)

    def test_profile(self):
        """ Test pour la page de profile """
        url = reverse('profile', kwargs={'username': 'DavWin'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)