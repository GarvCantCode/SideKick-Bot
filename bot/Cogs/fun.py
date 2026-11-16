import discord
from discord import app_commands
from discord.ext import commands

from bot.Lib.text import make_zalgo


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="zalgo", description="Make text look glitchy and cursed")
    async def zalgo(self, ctx: discord.Interaction, text: app_commands.Range[str, 1, 250], intensity: app_commands.Range[int, 1, 10]):
        msg =  make_zalgo(text=text, intensity=intensity)
        await ctx.response.send_message(msg)
    
    
async def setup(bot):
    await bot.add_cog(Fun(bot))