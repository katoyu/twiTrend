# ファイルをオープンする
test_data = open("NGword.txt")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()

print(lines[0])

# 一行ずつ表示する
for line in lines:
  line = line.replace('\n', '')
  line = "'"+line+"', \n"
  print(line)
with open("NGword.txt", mode='w') as f:
  f.writelines(lines)

print(lines)
# ファイルをクローズする
test_data.close()
