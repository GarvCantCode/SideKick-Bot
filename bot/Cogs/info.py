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
        
        msg = f"**{latency} ms** · up **{days}d {hours}h {minutes}m {seconds}s**"
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="info", description="Provides information about user")
    async def info(self, ctx: discord.Interaction, user: discord.Member | discord.User | None = None):
        embed = discord.Embed(title=user.display_name, color=discord.Colour.random())
        # first time creating an embed        

        embed.set_thumbnail(url=user.display_avatar)
        embed.add_field(name="Username", value=user.name)
        embed.add_field(name="ID",value=user.id)
        embed.add_field(name="Bot", value=user.bot)
        embed.add_field(name="Creation Date", value=discord.utils.format_dt(user.created_at, "R")) # change to whatever format you like
        
        await ctx.response.send_message(embed=embed)
        
        
        
async def setup(bot: commands.Bot):
    await bot.add_cog(DiscordTools(bot))