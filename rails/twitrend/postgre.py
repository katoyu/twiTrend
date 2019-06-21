import psycopg2

path = "localhost"
port = "5432"
dbname = "twitrend_development"
#user = "twitrend"
#password = "ENV['TWITREND_DATABASE_PASSWORD']"

conText = "host={} port={} dbname={} "
conText = conText.format(path,port,dbname)
connection = psycopg2.connect(conText)
cur = connection.cursor()

word = '筑波'
count = 2
created_at = '2019-06-21 00:00:00 UTC'
updated_at = '2019-06-21 00:00:00 UTC'

sql = 'insert into items(word, count, created_at, updated_at) values(%s, %s, %s, %s)'
cur.execute(sql, (word, int(count), created_at, updated_at))
connection.commit()

