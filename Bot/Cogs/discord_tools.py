from datetime import UTC, datetime, timezone

import discord
import psutil
from discord import app_commands
from discord.ext import commands


class DiscordTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.now(UTC)

    @app_commands.command(name="ping", description="Gives the bot latency")
    async def ping(self, ctx: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        msg = f"Latency: **{latency}ms**"
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="stats", description="Shows bot statistics")
    async def stats(self, ctx: discord.Interaction):
        uptime = datetime.now(UTC) - self.bot.launch_time
        days, remainder = divmod(int(uptime.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        cpu_header = psutil.cpu_percent(1) # cpu blocking call to retrive cpu info
        ram_header = psutil.virtual_memory()
        
        msg = f"CPU Usage: **{cpu_header}**%\nRAM Usage: **{ram_header.percent}**%\n Uptime: **{days}d {hours}h {minutes}m {seconds}s**"
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="timestamp", description="Converts timestamps into discord timestamp code")
    async def timestamp(self, ctx: discord.Interaction, style: str):
        now =  datetime.now(timezone.utc)
        stamp = discord.utils.format_dt(now, style=style)
        
        msg = f'Timestamp: **{stamp}**'
        await ctx.response.send_message(msg)
        
    
        
        
async def setup(bot):
    await bot.add_cog(DiscordTools(bot))