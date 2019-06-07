import json
import config
from requests_oauthlib import OAuth1Session

# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(ユーザータイムラインを取得する)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# Enedpointへ渡すパラメーター
params ={
        'count'       : 100,             # 取得するtweet数
        'screen_name' : 'ITF_katoyu',  # twitterアカウント名
       }

req = twitter.get(url, params = params)

if req.status_code == 200:
    res = json.loads(req.text)
    for line in res:
        #print(line['user']['name']+'::')
        print(line['text'])
        #print(line['created_at'])
        print('-----------------------------------------')
else:
    print("Failed: %d" % req.status_code)