import sys
import json
import config
import MeCab
from requests_oauthlib import OAuth1Session
import re
from collections import Counter
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
          "include_entities" : 0, #エンティティ(画像のURL等)をツイートに含めるか
          "exclude_replies" : 0, #リプライを含めるか
          }

req = sess.get(url, params=params)
timeline = json.loads(req.text)

data = ''
for tweet in timeline:
    #print(tweet["text"])
    data += tweet["text"].replace('\n', '')

print(data)


# =============================================================================
# MeCab
# =============================================================================
#req = MeCab.Tagger('-Owakati')
# パース
mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)

count = 100 #表示単語数
count2 = 100

# 名詞をリストに格納
words = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '名詞' and item[2] == '一般')]

#形容詞をリストに格納
words2 = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '形容詞')]

# 頻度順に出力
print("名詞")
counter = Counter(words)
for word, count in counter.most_common(count):
    print(f"{word}: {count}")

'''
print("形容詞")
counter2 = Counter(words2)
for word2, count2 in counter2.most_common(count2):
    print(f"{word2}: {count2}")
'''
# 形態素解析
#print(req.parse(result))