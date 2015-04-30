from kafka import SimpleProducer, KafkaClient, KafkaConsumer
from flask import Flask
import sys
import logging
logging.basicConfig()

app= Flask(__name__)
kafka = KafkaClient("localhost:9092")

def produce():
    producer = SimpleProducer(kafka,async=False,req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE,ack_timeout=2000)
    for pokeman in ["pikachu","bulbasur","charmander","squirtle"]:
        response = producer.send_messages("pokemans",pokeman)
        print(response)

def consume():
    consumer = KafkaConsumer("pokemans",group_id="best_group",metadata_broker_list=["localhost:9092"])
    for message in consumer:
        print(message)

@app.route("/")
def serve():
    return "hello world!"

if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'produce':
        produce()
    if command == 'consume':
        consume()
    if command == 'serve':
        app.run(host='0.0.0.0')
    else:
        print("NO COMMAND")
    kafka.close()
