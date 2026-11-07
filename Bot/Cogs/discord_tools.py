import discord
from discord import app_commands
from discord.ext import commands


class DiscordTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="ping", description="Gives the bot latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        msg = f"Pong! Latency is **{latency}ms**"
        await interaction.response.send_message(msg)
        

async def setup(bot):
    await bot.add_cog(DiscordTools(bot))