from flask import Flask, jsonify
import pika
from threading import Lock

app = Flask(__name__)

class ConsumerService:
    def __init__(self):
        self.lock = Lock()
        self.builder = ["[Python-Flask] no messages for now<br>"]

    def consume(self, ch, method, properties, body):
        message = body.decode()
        info = f"[Python-Flask] message consumed = \"{message}\"<br>"
        print(info) # Para ver desde consola
        with self.lock:
            self.builder.append(info)

    def get_info(self):
        with self.lock:
            return ''.join(self.builder)

# Create an instance of the ConsumerService
consumer_service = ConsumerService()

# Set up RabbitMQ connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='broker-1'))
channel = connection.channel()
channel.queue_declare(queue='my_queue')  # Ensure the queue exists (Si ya existe salta error)
channel.basic_consume(queue='my_queue', on_message_callback=consumer_service.consume, auto_ack=True)

# Start consuming messages in a separate thread
def start_consuming():
    channel.start_consuming()

import threading
threading.Thread(target=start_consuming, daemon=True).start()

@app.route('/consumed/messages', methods=['GET'])
def consumed_messages():
    return consumer_service.get_info()

if __name__ == '__main__':
    app.run(host='localhost', port=8082)