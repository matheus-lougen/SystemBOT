import discord
import time
from typing import Optional
from discord.ext import commands

from .modules import logger
from .modules import config


class Client(commands.Bot):
    def __init__(self,
                 config: config,
                 initial_extensions: Optional[tuple] = None):

        self.initial_extensions = initial_extensions
        self.config = config
        self.log = logger.get('main')
        self.extension_log = logger.get('extensions')
        self.discord_log = logger.get('discord')
        self.discord_https_log = logger.get('discord.https')

        # Calling the constructor method from the base class
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            intents=discord.Intents.all(),
            help_command=None,
        )

    async def setup_hook(self) -> None:
        if isinstance(self.initial_extensions, type(None)):
            self.extension_log.info('No initial extensions especified to load')
        elif len(self.initial_extensions) == 1:
            await self._load_extension(self.initial_extensions[0])
        else:
            for extension in self.initial_extensions:
                await self._load_extension(extension)

    async def _load_extension(self, extension: str) -> str:
        try:
            await self.load_extension(f'{extension}')
        except Exception as error:
            self.extension_log.exception(f'An error ocurred while loading the extension: [{extension}]')
            return f'An error ocurred while loading the extension: ``[{extension}]``'
        else:
            self.extension_log.info(f'Loaded extension: [{extension}]')
            return f'Loaded extension: ``[{extension}]``'

    async def _unload_extension(self, extension: str) -> None:
        try:
            await self.unload_extension(f'{extension}')
        except Exception as error:
            self.extension_log.exception(f'An error ocurred while unloading the extension: [{extension}]')
            return f'An error ocurred while unloading the extension: ``[{extension}]``'
        else:
            self.extension_log.info(f'Unloaded extension: [{extension}]')
            return f'Unloaded extension: ``[{extension}]``'

    async def _reload_extension(self, extension: str) -> None:
        try:
            await self.reload_extension(f'{extension}')
        except Exception as error:
            self.extension_log.exception(f'An error ocurred while reloading the extension: [{extension}]')
            return f'An error ocurred while reloading the extension: ``[{extension}]``'
        else:
            self.extension_log.info(f'Reloaded extension: [{extension}]')
            return f'Reloaded extension: ``[{extension}]``'

