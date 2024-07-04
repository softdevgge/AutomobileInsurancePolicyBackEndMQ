import pika

def send_message(message):
    credentials = pika.PlainCredentials('usermq', 'passwordmq')
    parameters = pika.ConnectionParameters('172.17.0.2',
                                   5672,
                                   '/',
                                   credentials)
    connection = pika.BlockingConnection(parameters)    
    channel = connection.channel()

    channel.queue_declare(queue='insurance_quotes')

    channel.basic_publish(exchange='', routing_key='insurance_quotes', body=message)
    print(" [x] Sent %r" % message)

    connection.close()
