from kafka import SimpleConsumer, KafkaClient

kafka = KafkaClient("10.42.2.106:9092")
consumer = SimpleConsumer(kafka,"test-group","updates")
kafka.ensure_topic_exists('updates')

for message in consumer:
    print(message)
