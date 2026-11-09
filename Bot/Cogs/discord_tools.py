from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands


class DiscordTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.utcnow()

    @app_commands.command(name="ping", description="Gives the bot latency")
    async def ping(self, ctx: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        msg = f"Latency: **{latency}ms**"
        await ctx.response.send_message(msg)

    @app_commands.command(name="uptime", description="Give the bot uptime")
    async def uptime(self, ctx: discord.Interaction):
        total_uptime = datetime.utcnow() - self.bot.launch_time
        days, remainder = divmod(int(total_uptime.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        msg = f"Uptime: **{days}days {hours}hours {minutes}minutes {seconds}seconds**"
        await ctx.response.send_message(msg)
        
async def setup(bot):
    await bot.add_cog(DiscordTools(bot))