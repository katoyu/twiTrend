import MeCab

req = MeCab.Tagger('-Owakati')
res = req.parse("昨日はモスバーガーを食べたので、 今日はマックを食べたいですね。")

print(res)

tokenizer = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
tokenizer.parse("")
node = tokenizer.parseToNode(document)
keywords = []
while node:
    if node.feature.split(",")[0] == u"名詞":
        keywords.append(node.surface)
    elif node.feature.split(",")[0] == u"形容詞":
        keywords.append(node.feature.split(",")[6])
    elif node.feature.split(",")[0] == u"動詞":
        keywords.append(node.feature.split(",")[6])
    node = node.next