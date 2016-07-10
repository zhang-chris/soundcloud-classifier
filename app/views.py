from django.shortcuts import render, redirect
import soundcloud_api

# Create your views here.
def index(request):
    return render(request, 'index.html')

def soundCloudAuth(request):
    apiCall = soundcloud_api.authSoundCloud()
    return redirect(apiCall)