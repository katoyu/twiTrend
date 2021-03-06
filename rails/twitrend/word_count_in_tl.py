#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import config
import MeCab
from requests_oauthlib import OAuth1Session
import re
from collections import Counter
from urllib import request
import psycopg2
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

f = open("NGword.txt")
data1 = f.read()
f.close()
ngword = data1.split('\n')


#DBとの接続、developmentなので下二つは未設定

path = "localhost"
port = "5432"
dbname = "twitrend_development"
#user = ""
#password =""

# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
sess = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(ホームタイムラインを取得する)
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {"count":200, #ツイートを最新から何件取得するか(最大200件)
          "include_entities" : False , #エンティティ(画像のURL等)をツイートに含めるか
          "exclude_replies" : 0, #リプライを含めるか
          }

req = sess.get(url, params=params)
timeline = json.loads(req.text)

data = ''
for tweet in timeline:
    #print(tweet["text"])
    data += tweet["text"].replace('\n', '') #全てを一つのデータにまとめる

print(data) #まとめたものを表示

# MeCab
#req = MeCab.Tagger('-Owakati')
# パース
mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)

count = 30 #表示単語数

# 名詞をリストに格納
words = [item[0]
         for item in items
            if len(item) >= 3 and (item[0] not in (ngword) and
             item[1] == '名詞' and item[2] == '一般')]
#DBへの接続準備
conText = "host={} port={} dbname={}"
conText = conText.format(path,port,dbname)
connection = psycopg2.connect(conText)
cur = connection.cursor()

# 頻度順に出力
print("名詞")
counter = Counter(words)
for word, count in counter.most_common(count):
    #print(f"{word}: {count}")

    created_at = date
    updated_at = date
    sql = 'insert into items(word, count, created_at, updated_at) values(%s, %s, %s, %s)'
    cur.execute(sql, (word, int(count), created_at, updated_at))
    connection.commit()



# 形態素解析
#print(req.parse(result))