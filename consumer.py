from confluent_kafka import Consumer

#configurations
config = {
    "bootstrap.servers":"localhost:9092",
    "group.id":6,
    "auto.offset.reset":"earliest"
}

#consumer client
consumer = Consumer(config)

#define topics and subscribe
topics = ["rohit-test"]
consumer.subscribe(topics)

#run consumer
while True:
    record = consumer.poll(1.0)
    if record is None:
        continue
    elif record.error():
        print(f"Error:{record.error()}")

    print(f"key:{record.key()}, value:{record.value()}, topic:{record.topic()}")

consumer.close()
