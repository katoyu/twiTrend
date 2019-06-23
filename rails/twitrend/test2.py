path_w = 'NGword.txt'

test_data = open(path_w)
lines = test_data.readlines()

with lines as f:
  # 一行ずつ表示する
  for line in lines:
    line = line.replace('\n', '')
    line = "'"+line+"', \n"

  f.write(line)

with open(path_w) as f:
    print(f.read())
# New file