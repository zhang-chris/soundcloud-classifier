from django.shortcuts import render, redirect
import soundcloudAPI


# Create your views here.
def index(request):
    return render(request, 'index.html')

def authLazyList(request):
    apiCall = soundcloudAPI.authSoundCloud()
    return redirect(apiCall)

def authSoundCloud(request):
	code = request.GET.get('code')
	accessToken = soundcloudAPI.exchangeToken(code)
	newClient = soundcloudAPI.userInfo(accessToken)
	# TODO: Need to display favorites playlist, and then loop through songs
	# in playlist and run song through classification algorithm
	# Gives you name of songs in favorites
	favorites = newClient.get('/me/favorites')
	for song in favorites:
		for key, value in song.fields().items():
			if key == 'title':
				print value


def classification(song):
	pass