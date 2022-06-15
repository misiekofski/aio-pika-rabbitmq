import asyncio
import random
from time import sleep

import aio_pika

from MessageData import MessageData


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    async with connection:
        message = MessageData().get_json()
        routing_key = "hello"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key,
        )


if __name__ == "__main__":
    while True:
        asyncio.run(main())
        sleep(random.randint(3, 10))
