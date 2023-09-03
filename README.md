# Kafka with Python Setup in Less than 5 minutes

Step 1:
Clone `https://github.com/conduktor/kafka-stack-docker-compose`

Run `docker compose -f zk-single-kafka-single.yml up`

Step 2: 

Clone this project 

run Pip install -r requirements.txt

Up Faust worker `faust -A app worker -l info`
Produce Message faust -A app send hello_world 'Hello Folks, Raheel Here!'
