# Kafka with Python Setup in Less than 5 Minutes

This guide demonstrates a quick setup for working with Kafka and Python using Faust and Docker Compose. You can have Kafka up and running in just a few minutes following these steps.

## Step 1: Setting Up Kafka with Docker Compose

1. Clone the `kafka-stack-docker-compose` repository:

   ```shell
   git clone https://github.com/conduktor/kafka-stack-docker-compose
   
2. Navigate to the repository directory: 
    ```shell
    cd kafka-stack-docker-compose
3. Start Kafka and ZooKeeper containers:
    ```shell
    docker compose -f zk-single-kafka-single.yml up

## Step 2: Running the Python Kafka Setup

1. Clone this project:

   ```shell
   git clone https://github.com/rawheel/Kafka-Python-Example.git

2. Navigate to the project directory:
   ```shell
   cd Kafka-Python-Example
3. Install project dependencies:
   ```shell
   pip install -r requirements.txt
4. Start a Faust worker:
   ```shell
   faust -A worker worker -l info
5. To produce a Kafka message using the Faust command-line tool, run:
   ```shell
   faust -A worker send hello_world 'Hello Folks, Raheel Here!'

6. To produce kafka messages using python code
   ```shell
   python producer.py
