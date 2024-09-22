from flask import Flask, jsonify
from threading import Lock
import threading
import pika
import os

app = Flask(__name__)

class ConsumerService:
    def __init__(self):
        self.lock = Lock()
        self.builder = ["[Python-Flask] no messages for now<br>"]

    def consume(self, ch, method, properties, body):
        message = body.decode()
        info = f"[Python-Flask] message consumed = \"{message}\"<br>"
        print(info)
        with self.lock:
            self.builder.append(info)

    def get_info(self):
        with self.lock:
            return ''.join(self.builder)

# Create an instance of the ConsumerService
consumer_service = ConsumerService()

# Getting environment variables
BROKER_NAME = 'broker-1' #os.getenv('BROKER_NAME')
QUEUE_NAME = 'cola1'#os.getenv('QUEUE_NAME')

# Set up RabbitMQ connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_NAME))
channel = connection.channel()
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=consumer_service.consume, auto_ack=True)

# Start consuming messages in a separate thread
def start_consuming():
    channel.start_consuming()

threading.Thread(target=start_consuming, daemon=True).start()

@app.route('/consumed/messages', methods=['GET'])
def consumed_messages():
    return consumer_service.get_info()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)