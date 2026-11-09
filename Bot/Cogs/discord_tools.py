from datetime import datetime

import psutil
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
        
    @app_commands.command(name="stats", description="Shows bot statistics")
    async def stats(self, ctx: discord.Interaction):
        uptime = datetime.utcnow() - self.bot.launch_time
        days, remainder = divmod(int(uptime.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        cpu_header = psutil.cpu_percent(1) # cpu blocking call to retrive cpu info
        ram_header = psutil.virtual_memory()
        
        msg = f"CPU Usage: {cpu_header}%\nRAM Usage: {ram_header}%\n Uptime: {days}d {hours}h {minutes}m {seconds}s"
        await ctx.response.send_message(msg)
        
    
        
async def setup(bot):
    await bot.add_cog(DiscordTools(bot))