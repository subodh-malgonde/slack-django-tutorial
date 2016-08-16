from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .models import Team


# Create your views here.
def index(request):
    return render(request, 'landing.html', {})


def slack_oauth(request):
    code = request.GET['code']

    params = {
        'code': code,
        'client_id': "your_client_id",
        "client_secret": "your_client_secret"
    }
    url = 'https://slack.com/api/oauth.access'
    json_response = requests.get(url, params)
    data = json.loads(json_response.text)
    Team.objects.get_or_create(
        name=data['team_name'],
        team_id=data['team_id'],
        bot_user_id=data['bot']['bot_user_id'],
        bot_access_token=data['bot']['bot_access_token']
    )
    return HttpResponse('Bot added to your Slack team!')