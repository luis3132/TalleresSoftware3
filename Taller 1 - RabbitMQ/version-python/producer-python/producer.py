from flask import Flask
import pika

app = Flask(__name__)

class ProducerService:
    def __init__(self, queue_name, broker_host='broker-1'):
        self.queue = queue_name
        # Set up RabbitMQ connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker_host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue) # Ensure the queue exists (Si ya existe salta error)

    def publish(self, message):
        # Publish message to the specified queue
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)
        print(f"[Python-Flask] message published = \"{message}\"")

# Instantiate the ProducerService with the queue name
producer_service = ProducerService(queue_name='my_queue', broker_host='broker-1')

@app.route('/publish/<message>', methods=['GET'])
def publish_message(message):
    # Publish the message using the ProducerService
    producer_service.publish(message)
    info = f"[Python-Flask] message published = \"{message}\""
    return info

if __name__ == '__main__':
    # Start Flask app
    app.run(host='localhost', port=8081)
