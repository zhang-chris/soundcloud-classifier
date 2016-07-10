import soundcloud
import keys
from django.shortcuts import redirect


def authSoundCloud():
	client = soundcloud.Client(client_id = keys.CLIENT_ID,
                           		client_secret = keys.CLIENT_SECRET,
                           		redirect_url = 'http://localhost:8000/SoundCloudAuth')
	# redirect user to authorize URL
	return client.authorize_url()


