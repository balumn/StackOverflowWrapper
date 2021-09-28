import requests
from django.conf import settings

def so_advanced_search(data):
    try:
        response = requests.get(settings.STACKOVERFLOW_URL, params=data)
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}