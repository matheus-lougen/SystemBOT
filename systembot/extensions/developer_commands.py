import discord
from discord import app_commands
from discord.ext import commands

import systembot
from .checks import is_owner


class DeveloperCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    extension = app_commands.Group(name='extension', description='Extensions related commands')

    @extension.command(name='load', description='load an extension')
    @is_owner()
    async def load(self, interaction: discord.Interaction, extension: str) -> None:
        await interaction.response.send_message(await self.client._load_extension(extension), ephemeral=True)

    @extension.command(name='unload', description='unload an extension')
    @is_owner()
    async def unload(self, interaction: discord.Interaction, extension: str) -> None:
        await interaction.response.send_message(await self.client._unload_extension(extension), ephemeral=True)

    @extension.command(name='reload', description='reload an extension')
    @is_owner()
    async def load(self, interaction: discord.Interaction, extension: str) -> None:
        await interaction.response.send_message(await self.client._reload_extension(extension), ephemeral=True)

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx, arg=None):
        await ctx.message.delete()
        if arg == 'global':
            synced = await ctx.bot.tree.sync()
            self.log.warning(f'Synced {len(synced)} commands globally')
        else:
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
            self.log.warning(f'Synced {len(synced)} commands on this guild')


async def setup(client: systembot.Client) -> None:
    await client.add_cog(DeveloperCommands(client))
