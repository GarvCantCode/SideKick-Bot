from datetime import UTC, datetime

import discord
from discord import app_commands
from discord.ext import commands


class DiscordTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.now(UTC)

    @app_commands.command(name="ping", description="Gives the bot latency")
    async def ping(self, ctx: discord.Interaction):
        uptime = datetime.now(UTC) - self.bot.launch_time
        days, remainder = divmod(int(uptime.total_seconds()), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        latency = round(self.bot.latency * 1000)
        
        msg = f"Pong: **{latency} ms** · up **{days}d {hours}h {minutes}m {seconds}s**"
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="timestamp", description="Converts timestamps into discord timestamp code")
    async def timestamp(self, ctx: discord.Interaction,msgf: str, style: str):
        now =  datetime.now(UTC)
        stamp = discord.utils.format_dt(now, style=style)
        
        msg = f'{msgf} **{stamp}**'
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="info", description="Provides detailed information about user")
    async def info(self, ctx: discord.Interaction, user: discord.Member | discord.User | None = None):
        # first time creating an embed
        embed = discord.Embed(title=user.display_name, color=discord.Colour.random())
        embed.set_thumbnail(url=user.display_avatar)
        embed.add_field(name="Username", value=user.name)
        embed.add_field(name="ID",value=user.id)
        embed.add_field(name="Bot", value=user.bot)
        embed.add_field(name="Creation Date", value=discord.utils.format_dt(user.created_at, "R"))
        
        await ctx.response.send_message(embed=embed)
        
        
        
async def setup(bot):
    await bot.add_cog(DiscordTools(bot))