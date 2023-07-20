def test_dummy():
    assert 1
# --/////////////////////////////////////////////////////////////////////////////////////////////////--

import pytest
from django.test import Client

client = Client()

def test_index(client):
    """ Test pour la page d'accueil """
    response = client.get('/')
    html_content = response.content
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in html_content