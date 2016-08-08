import soundcloud
import keys
from django.shortcuts import redirect

client = soundcloud.Client(client_id = keys.CLIENT_ID,
                           client_secret = keys.CLIENT_SECRET,
                           redirect_url = 'http://localhost:8000/SoundCloudAuth')

def authSoundCloud():
	return client.authorize_url()

def exchangeToken(code):
	return client.exchange_token(code).access_token

def userInfo(accessToken):
	newClient = soundcloud.Client(access_token = accessToken)
	return newClient




