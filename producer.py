from confluent_kafka import Producer

#properties
config = {
    "bootstrap.servers":'localhost:9092',
    "acks":'all'
}

#callback handler
def callback_action(error, msg):
    if error is None:
        print(f"topic is {msg.topic()} , partition:{msg.partition()} ")
    else:
        print(f"Error is {error}")

#producer client
producer = Producer(config)

#produce message
producer.produce(topic='rohit-test',
                 key='3',
                 value="hi rohit! This is callback 4",
                 partition=0,
                 callback=callback_action)

#to flush all the pending messages in buffer
producer.flush()