"""
MIT License

Copyright (c) 2023 Matheus Lougen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
from typing import Any, Coroutine, Optional, MutableMapping

import discord
from discord.ext import commands

from systembot.modules import logger

log = logger.create(
    __name__, level=logger.DEBUG, handlers=[logger.StreamHandler(), logger.FileHandler(f'./data/logs/{__name__}.log')]
)


class Client(commands.Bot):
    """Represents a Discord bot.
    This class is a subclass of discord.ext.commands.Bot"""

    def __init__(self, config: MutableMapping, initial_extensions: Optional[tuple]) -> None:
        self.initial_extensions: Optional[tuple] = initial_extensions
        self.config: MutableMapping = config

        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            help_command=None,
        )

    async def setup_hook(self) -> Coroutine[Any, Any, None]:
        """Executed only once on the client's setup"""
        for extension in self.initial_extensions:
            await self.load_extension(extension)

    async def load_extension(self, name: str, *, package: Optional[str] = None) -> Coroutine[Any, Any, None]:
        """Loads an extension.
        An extension is a python module that contains commands, cogs, or listeners.
        """
        try:
            start_time = time.process_time()
            await super().load_extension(f'systembot.extensions.{name}')
            load_time = time.process_time() - start_time
        except (
            commands.ExtensionAlreadyLoaded,
            commands.ExtensionNotFound,
            commands.ExtensionFailed,
            commands.NoEntryPointError,
        ):
            log.exception('An error ocurred while trying to load the EXTENSION: [%s]', name)
        else:
            log.info('Sucessfully loaded the EXTENSION: [systembot.extensions.%s] in %s seconds', name, load_time)

    async def unload_extension(self, name: str, *, package: Optional[str]) -> Coroutine[Any, Any, None]:
        """Unloads an extension.
        When the extension is unloaded, all commands, listeners, and cogs are removed from the bot and the module is
        un-imported
        """
        try:
            await super().unload_extension(f'systembot.extensions.{name}')
        except (
            commands.ExtensionAlreadyLoaded,
            commands.ExtensionNotFound,
            commands.ExtensionFailed,
            commands.NoEntryPointError,
        ):
            log.exception('An error ocurred while unloading the EXTENSION: [systembot.extensions.%s]', name)
        else:
            log.info('Sucessfully unloaded the EXTENSION: [systembot.extensions.%s]', name)

    async def reload_extension(self, name: str, *, package: Optional[str]) -> Coroutine[Any, Any, None]:
        """Reloads an extension.
        This replaces the extension with the same extension, only refreshed. This is equivalent to a unload_extension
        followed by a load_extension
        """
        try:
            start_time = time.process_time()
            await super().reload_extension(f'systembot.extensions.{name}')
            reload_time = time.process_time() - start_time
        except (
            commands.ExtensionAlreadyLoaded,
            commands.ExtensionNotFound,
            commands.ExtensionFailed,
            commands.NoEntryPointError,
        ):
            log.exception('An error ocurred while reloading the EXTENSION: [systembot.extensions.%s]', name)
        else:
            log.info('Sucessfully reloaded the EXTENSION: [systembot.extensions.%s] in %s seconds', name, reload_time)
