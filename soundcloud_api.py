import soundcloud
import keys

client = soundcloud.Client(client_id = keys.CLIENT_ID,
                           client_secret = keys.CLIENT_SECRET,
                           redirect_url = 'http://google.com')


