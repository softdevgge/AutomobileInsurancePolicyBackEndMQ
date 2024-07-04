from django.core.management.base import BaseCommand, CommandError
import logging

logger = logging.getLogger(__name__)
logger.critical("Now logging consumer command")

class Command(BaseCommand):
    help = "Process a  mq of quotes"


    def add_arguments(self, parser):
        parser.add_argument("numthreads", nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write("consumer command")
        logger.critical("ready ....")

        import pika, sys, os        
        import concurrent.futures        

        # RabbitMQ connection parameters
        credentials = pika.PlainCredentials('usermq', 'passwordmq')
        parameters = pika.ConnectionParameters('172.17.0.2',
                                   5672,
                                   '/',
                                   credentials)
        queue_name = 'insurance_quotes'
        from insurance_app import processrabbitmq
        
        def callback(ch, method, properties, body):
            logger.critical(" Received body = %s ", body)
            logger.critical(" [x] Received properties = %s ", properties)
            logger.critical(" [x] Received method = %s ", method)
            processrabbitmq.calcule_quote(ch, method, properties, body)

        
        # Function to consume messages from the RabbitMQ queue
        def consume():
            connection = pika.BlockingConnection(parameters)    
            channel = connection.channel()
            channel.queue_declare(queue=queue_name)
            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            logger.critical(f"Waiting for messages in {queue_name}. To exit press CTRL+C")
            channel.start_consuming()

        # Set up a multithreaded daemon to monitor the RabbitMQ queue
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future = executor.submit(consume)
            try:
                future.result()  # This will wait for the consume function to finish
                logger.critical("OOOOOOOOOOOOOOOOOOOOOOOOO thread completed! OOOOOOOOOOOOOOOOOOOO")
            except Exception as e:
                logger.error("OOOOOOOOOOOOOOOOOOOOOO error %s OOOOOOOOOOOOOOOOOOOO", e, exc_info=1)

        
            self.stdout.write(
                self.style.SUCCESS('Successfully started daemon ')
            )        


