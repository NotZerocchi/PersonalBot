import tweepy

CONSUMER_KEY = '4y0PH8sc0jDYX13rKYwKDg'
CONSUMER_SECRET = 'lnCP7qtbgSM3gIKiEIpEvr2fuQiWpI5H71gfpuy2s'
ACCESS_KEY = '126876549-yqLaAS6Qk844F3PaUkcahIKJ0DfG0023UIQV6o3s'
ACCESS_SECRET = 'I6gpupvn83iFJ7b0u9Haty2CZYyisXAq359rqtwgd04db'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

def tweet(txt):
	api = tweepy.API(auth)
	api.update_status(txt)

def mention():
	api = tweepy.API(auth)
	user_mention = api.mentions_timeline()
	for i in user_mention:
		print i.text, "\n"

def twtprofile():
	api = tweepy.API(auth)
	print api.me()
