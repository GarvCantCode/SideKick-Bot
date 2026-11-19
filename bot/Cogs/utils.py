from datetime import UTC, datetime

import discord
from discord import app_commands
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @app_commands.command(name="timestamp", description="Converts timestamps into discord timestamp code")
    async def timestamp(self, ctx: discord.Interaction,msgf: str, style: str):
        now =  datetime.now(UTC)
        stamp = discord.utils.format_dt(now, style=style)
        
        msg = f'{msgf} **{stamp}**'
        await ctx.response.send_message(msg)
        
async def setup(bot):
    await bot.add_cog(Utils(bot))