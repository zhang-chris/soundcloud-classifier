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
	print newClient.get('/me').username
