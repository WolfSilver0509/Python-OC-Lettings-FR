from django.test import Client
from django.urls import reverse
import pytest

client = Client()

@pytest.mark.django_db
def test_lettings_index(client):
    """ Test pour la page d'accueil """
    url = reverse('lettings_index')  # Utilisation de la fonction reverse pour récupérer l'URL par son nom
    response = client.get(url)
    html_content = response.content
    assert response.status_code == 200
    assert b"Lettings" in html_content


@pytest.mark.django_db
def test_lettings(client):
    """ Test pour la page de lettings """
    url = reverse('letting', kwargs={'letting_id': 1})
    response = client.get(url)
    html_content = response.content
    assert response.status_code == 200



