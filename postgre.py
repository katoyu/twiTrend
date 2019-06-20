import psycopg2

path = "localhost"
port = "5432"
dbname = "twitrend_production"
user = "twitrend"
password = "ENV['TWITREND_DATABASE_PASSWORD']"

conText = "host={} port={} dbname={} user={} password={}"
conText = conText.format(path,port,dbname,user,password)

connection = psycopg2.connect(conText)
cur = connection.cursor()