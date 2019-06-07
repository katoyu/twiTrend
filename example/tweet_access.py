import json
import config
from requests_oauthlib import OAuth1Session
from urllib import request

# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
sess = OAuth1Session(CK, CS, AT, ATS)
#sess = OAuth1Session(keys["CK"], keys["CS"], keys["AT"], keys["AS"])

# Twitter Endpoint(ホームタイムラインを取得する)
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {"count":200, #ツイートを最新から何件取得するか(最大200件)
          "include_entities" : 1, #エンティティ(画像のURL等)をツイートに含めるか
          "exclude_replies" : 1, #リプライを含めるか
          }

req = sess.get(url, params=params)
timeline = json.loads(req.text)

for tweet in timeline:
    print(tweet["text"])