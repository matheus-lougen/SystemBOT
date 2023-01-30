import discord
from discord import app_commands

def is_owner():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 346244061872652289
    return app_commands.check(predicate)