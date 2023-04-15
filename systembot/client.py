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
        await self.load_extension('jishaku')
        for extension in self.initial_extensions:
            await self.load_extension(extension)
