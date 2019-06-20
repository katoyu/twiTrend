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

sql = "insert into items(word,count,created_at,updated_at) values('ITF.',100, '2019-06-19 07:27:49 UTC', '2019-06-19 07:27:49 UTC');"
cur.execute(sql)
connection.commit()