import sys
import json
import config
import MeCab
from requests_oauthlib import OAuth1Session
import re
from collections import Counter

# =============================================================================
# 引数の処理
# =============================================================================
# 第一引数を検索キーワードに設定
param = sys.argv
keyword = param[1]

# 第二引数を取得するtweet数に設定
param = sys.argv
tweetcount = param[2]

# =============================================================================
# Twitter API
# =============================================================================
# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(検索結果を取得する)
url = 'https://api.twitter.com/1.1/search/tweets.json'

# Enedpointへ渡すパラメーター
params ={
         'q'     : keyword,    # 検索キーワード
         'count' : tweetcount, # 取得するtweet数
         }

req = twitter.get(url, params = params)
data = ''
if req.status_code == 200:
    res = json.loads(req.text)
    data = ''
    for line in res['statuses']:
        # 改行コードを削除
        text = line['text'].replace('\n','')
        # resultに足しこんでいく(1行にしたいので)
        data += text
else :
    print("Failed: %d" % req.status_code)

# =============================================================================
# MeCab
# =============================================================================
#req = MeCab.Tagger('-Owakati')
# パース
mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)

count = 20 #ループ回数

# 名詞をリストに格納
words = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '名詞' and item[2] == '一般')]

# 頻度順に出力
counter = Counter(words)
for word, count in counter.most_common(count):
    print(f"{word}: {count}")

# 形態素解析
#print(req.parse(result))