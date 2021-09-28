import requests
from django.conf import settings
from datetime import datetime
from django.contrib import messages

def so_advanced_search(data):
    try:
        response = requests.get(settings.STACKOVERFLOW_URL, params=data)
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}

def monitor_search(request):
    now     = datetime.now()
    minute  = request.session.get(str(now.minute))
    day     = request.session.get(str(now.day))
    request.session.clear()
    
    if minute != None:
        request.session[str(now.minute)] = minute + 1
    else:
        request.session[str(now.minute)] = 1
    
    if day is not None:
        request.session[str(now.day)] = day + 1
    else:
        request.session[str(now.day)] = 1

    if request.session[str(now.minute)] > settings.PER_MINUTE_LIMIT:
        messages.error(request, f"Per minute Search Limit of {settings.PER_MINUTE_LIMIT} Exceeded")
        return False
    if request.session[str(now.minute)] > settings.PER_DAY_LIMIT:
        messages.error(request, f"Per day Search Limit of {settings.PER_DAY_LIMIT} Exceeded")
        return False
    return True
