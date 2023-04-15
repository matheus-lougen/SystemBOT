#!/usr/bin/env python

import asyncio
from typing import NoReturn

import configparser
from discord.ext import commands

from systembot.client import Client
from systembot.modules import logger

log = logger.create(
    __name__, level=logger.DEBUG, handlers=[logger.StreamHandler(), logger.FileHandler(f'./data/logs/{__name__}.log')]
)


def main() -> None:
    """Main function"""
    logger.create(
        'wavelink', level=logger.WARNING, handlers=[logger.StreamHandler(), logger.FileHandler('./data/logs/wavelink.log')]
    )
    logger.create(
        'wavelink.websocket',
        level=logger.WARNING,
        handlers=[logger.StreamHandler(), logger.FileHandler('./data/logs/wavelink.log')],
    )
    logger.create(
        'discord', level=logger.WARNING, handlers=[logger.StreamHandler(), logger.FileHandler('./data/logs/discord.log')]
    )
    logger.create(
        'discord.https',
        level=logger.WARNING,
        handlers=[logger.StreamHandler(), logger.FileHandler('./data/logs/discord.https.log')],
    )

    initial_extensions = (
        'systembot.extensions.commands.user_commands',
        'systembot.extensions.music.commands',
        'systembot.extensions.music.events',
        'systembot.extensions.music.exceptions',
    )

    config = configparser.ConfigParser()
    config.read('./data/config.ini')
    client = Client(config, initial_extensions)
    asyncio.run(run_bot(client))


async def run_bot(client: commands.Bot) -> NoReturn:
    async with client:
        await client.start(client.config['discord']['token'])


if __name__ == '__main__':
    main()
