

# Back end of automobile insurance policy
## Problem :
Generates an "automobile insurance policy" quote system  using Angular 16, RabbitMQ, and Python Django Rest API with JWT security


## Explanation

### Setup RabbitMQ

Ensure RabbitMQ is installed and running on your machine. 

docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=usermq -e RABBITMQ_DEFAULT_PASS=passwordmq rabbitmq:3-management



### PYTHON ENVIRONMENT

pipenv shell

pipenv install -r requirements.txt



**Create and Apply Migrations**

pipenv run python manage.py makemigrations

pipenv run python manage.py migrate

......./insurance_project$ pipenv run python manage.py runserver



### RUN RABITMQCONSUMER AS A COMMAND

......./insurance_project$pipenv run python manage.py consumequote  5
