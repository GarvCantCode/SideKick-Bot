import io
from datetime import UTC, datetime
from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from src.helpers.base64 import convert


class Utils(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @app_commands.command(name="timestamp", description="Converts timestamps into discord timestamp code")
    async def timestamp(self, ctx: discord.Interaction,msgf: str, style: Literal["t", "T", "d", "D", "f", "F", "R"]):
        now =  datetime.now(UTC)
        stamp = discord.utils.format_dt(now, style=style)
        
        msg = f'{msgf} **{stamp}**'
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="base64", description="Encodes or decodes base64")
    async def base64(self, ctx: discord.Interaction, value: app_commands.Range[str,1,1500], mode: Literal["encode", "decode"]):
        await ctx.response.defer()
        
        file = discord.File(io.BytesIO(convert(mode, value).encode("utf-8")), filename=f"base64_{mode}d.txt")
        await ctx.followup.send(file=file, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot))