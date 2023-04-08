#!/usr/bin/env python

import asyncio
from typing import NoReturn

import systembot
from systembot.modules import logger
from systembot.modules import Config


def setup_logging() -> None:
    """Setup discord and wavelink loggers"""
    logger.create('wavelink',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(),
                            logger.FileHandler('./data/logs/wavelink.log')])
    logger.create('wavelink.websocket',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(),
                            logger.FileHandler('./data/logs/wavelink.log')])
    logger.create('discord',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(),
                            logger.FileHandler('./data/logs/discord.log')])
    logger.create('discord.https',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(),
                            logger.FileHandler('./data/logs/discord.https.log')])


def main() -> None:
    initial_extensions = (
        'commands.developer_commands',
        'commands.user_commands',
        'music.commands',
        'music.events',
        'music.exceptions',
        )

    setup_logging()
    client = systembot.Client(config=Config(path='./data/config.yaml'), initial_extensions=initial_extensions)
    asyncio.run(run_bot(client))


async def run_bot(client: systembot.Client) -> NoReturn:
    async with client:
        await client.start(client.config.token)


if __name__ == '__main__':
    main()
