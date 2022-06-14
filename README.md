# RabbitMQ + asyncio + aiopika 

## Requirements
Python 3.9+

## How to install

1. `git clone` repo
2. `docker-compose up` to run RabbitMQ
3. go to http://localhost:15672 to see rabbitMQ web UI
4. create new `Durable` queue with `Auto delete` set to `No` - named `hello`
5. from `client` folder run `python send.py`
6. from `server` folder run `python receiver.py`