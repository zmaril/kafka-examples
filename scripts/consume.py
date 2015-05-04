from kafka import SimpleConsumer, KafkaClient
import psycopg2 
kafka = KafkaClient("10.42.2.106:9092")
consumer = SimpleConsumer(kafka,"test-group","updates")

conn = psycopg2.connect("dbname=postgres user=postgres")
curs = conn.cursor()

try:    
    curs.execute("CREATE TABLE props (id serial PRIMARY KEY, prop varchar(10))")
    curs.commit()
except Exception:
    print "Table already created, roll 'em on back'"
    conn.rollback()

try:
    curs.execute("INSERT INTO props (id,prop) values (1,'')")
    conn.commit()
except Exception:
    print "Test row already created, roll it on back'"
    conn.rollback()
    
kafka.ensure_topic_exists('updates')

for om in consumer:
    prop = eval(om.message.value)
    print(prop[1])
    curs.execute("UPDATE props SET prop = '{0}' where id = 1".format(prop[1]))
    conn.commit()
