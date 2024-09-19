from flask import Flask
import os
import pika

app = Flask(__name__)

class ProducerService:
    def __init__(self, queue_name, broker_host):
        self.queue = queue_name
        # Set up RabbitMQ connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_host))
        self.channel = self.connection.channel()

    def publish(self, message):
        # Publish message to the specified queue
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
        print(f"[Python-Flask] message published = \"{message}\"")

# Getting environment variables
BROKER_NAME = 'broker-1' #os.getenv('BROKER_NAME')
QUEUE_NAME = 'cola1'#os.getenv('QUEUE_NAME')

# Instantiate the ProducerService with the queue name
producer_service = ProducerService(queue_name='cola1', broker_host='broker-1')
#producer_service = ProducerService(queue_name=QUEUE_NAME, broker_host=BROKER_NAME)

@app.route('/publish/<message>', methods=['GET'])
def publish_message(message):
    # Publish the message using the ProducerService
    producer_service.publish(message)
    info = f"[Python-Flask] message published = \"{message}\""
    return info

if __name__ == '__main__':
    # Start Flask app
    app.run(host='0.0.0.0', port=8081)
