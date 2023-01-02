from twitter import *
import key
import os
from t2v import voice2text

CONSUMER_KEY = key.api_key
CONSUMER_SECRET = key.api_key_secret
BEARER_TOKEN = key.bearer_token
MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
	oauth_dance("your_dance_name", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)
oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Get your "home" timeline
x = t.statuses.home_timeline(count=10)
# Get a particular friend's timeline
# x = t.statuses.user_timeline(screen_name="boogheta",count=5)
print(len(x))

for raw_msg in x:
	# msg = json.dumps(raw_msg)
	# print(raw_msg)
	twitter_name = raw_msg['user']['name']
	twitter_text = raw_msg['text'].replace('\r', '').replace('\n', '').split('https')[0]
	# print(raw_msg['created_at'], twitter_name, twitter_text, sep=':', end='\n')
	myTuple = (twitter_name, "说", twitter_text)
	text2BProcess = ",".join(myTuple)
	voice2text(text2BProcess)
