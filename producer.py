import uuid
from kafka import KafkaProducer

BROKER = '0.0.0.0:9092'
TOPIC = 'hello_world'

def publish_message(producer_instance, key, value, topic=TOPIC):

    """
    Publish message to the consumer/worker with a particular topic
    """
    print("came to publish_message")

    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic, key=key_bytes, value=value_bytes)
        producer_instance.flush()

        return 'Message published successfully'
    except Exception as e:
        return f'Can not publish message successfully, {e}'


def connect_kafka_producer():

    """
    connects the server and returns the producer instance
    """
    print("came to connect_kafka_producer")
    _producer = None

    try:
        _producer = KafkaProducer(bootstrap_servers=BROKER)
    except Exception as e:
        return f'Exception while connecting Kafka, {e}'
    return _producer

if __name__ == '__main__':
    kafka_producer = connect_kafka_producer()
    for i in range(10):
        message = f"Hello World, Raheel Here!, {i}"
        key = str(uuid.uuid4())
        publish_message(kafka_producer, key, message)
    if kafka_producer is not None:
        kafka_producer.close()