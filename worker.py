import faust

# Create a Faust application named 'myapp' and configure it to use Kafka broker '0.0.0.0:9092'.
# auto_create_topics=True allows Faust to create the topic if it doesn't exist.
app = faust.App('myapp', broker='0.0.0.0:9092', auto_create_topics=True)


# Define a topic named 'hello_world' with a value type of 'str'.
# 'value_serializer' specifies how the value will be serialized. 'raw' means it's plain text.
topic = app.topic('hello_world', value_type=str, value_serializer='raw')

# Define an agent that processes messages from the 'hello_world' topic.
# This agent will consume messages from the topic and perform some action on them.
@app.agent(topic)
async def processor(stream):
    # 'stream' is an asynchronous generator that yields messages from the topic.
    async for message in stream:
        # Process each message received from the topic.
        # In this example, we simply print the received message.
        print(f'Received {message}')
