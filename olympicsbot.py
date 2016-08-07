import tweepy, time, datetime, olympicsdata
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

today = datetime.date.today()
laststatus = ''

while (today.isoformat() != '2016-08-22'):
	olympicsdata.updateData()
	filename = open('olympics.txt', 'r')
	tweettext = filename.readlines()
	filename.close()

	tweet = ''
	count = 1
	for line in tweettext[0:5]:
		tweet = tweet + str(count) + "." + line
		count += 1
	
	if (tweet == laststatus):
		print "skipping tweet"
	else:	
		api.update_status(status=tweet)
		laststatus = tweet
		print tweet
	time.sleep(60)
