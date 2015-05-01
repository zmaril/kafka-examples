from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient("10.42.2.106:9092")
producer = SimpleProducer(kafka)
kafka.ensure_topic_exists('updates')

class Journaled(object):
    def send_update(self, name, value):
        print (name,value)
        producer.send_messages('updates',str((name,value)))
        return (True,"Message")

    def __setattr__(self,name,value):
        result = self.send_update(name,value)        
        if result[0] == True:            
            super(Journaled,self).__setattr__(name,value)
        else:
            raise Exception("$1 cannot be set to $2 due to the following error: \n $3".format(name,value, result[1]))

j = Journaled()
j.prop = "prop"
