#!/usr/bin/env python

import logging
import asyncio

import discord

from systembot import Client
from systembot.modules import logger
from systembot.modules import Config


def setup_logging():
    formatter = logger.Formatter('%(asctime)s %(name)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s')
    colored_formatter = logger.ColoredFormatter(
        '%(light_green)s%(asctime)s %(red)s%(name)s %(log_color)s%(levelname)s %(yellow)s[%(filename)s:%(lineno)d]%(reset)s %(message)s'
        )
    logger.create('main',
                  level=logger.DEBUG,
                  handlers=[logger.StreamHandler(formatter=colored_formatter),
                            logger.FileHandler('./data/logs/main.log', formatter=formatter)])
    logger.create('extensions',
                  level=logger.DEBUG,
                  handlers=[logger.StreamHandler(formatter=colored_formatter),
                            logger.FileHandler('./data/logs/extensions.log', formatter=formatter)])
    logger.create('discord',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(formatter=colored_formatter),
                            logger.FileHandler('./data/logs/discord.log', formatter=formatter)])
    logger.create('discord.https',
                  level=logger.WARNING,
                  handlers=[logger.StreamHandler(formatter=colored_formatter),
                            logger.FileHandler('./data/logs/discord.https.log', formatter=formatter)])
    log = logger.get('main')
    return log


def main():
    initial_extensions = (
        'systembot.extensions.developer_commands',
        'systembot.extensions.admin_commands'
    )

    log = setup_logging()
    client = Client(config=Config(path='./data/config.yaml'),
                    initial_extensions=initial_extensions)

    asyncio.run(run_bot(client))


async def run_bot(client):
    async with client:
        await client.start(client.config.token)


if __name__ == '__main__':
    main()
