import random

import discord
from discord import app_commands
from discord.ext import commands

from src.helpers.text import make_zalgo


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="zalgo", description="Make text look glitchy and cursed")
    async def zalgo(self, ctx: discord.Interaction, text: app_commands.Range[str, 1, 100], intensity: app_commands.Range[int, 1, 10]):
        msg =  make_zalgo(text=text, intensity=intensity)
        await ctx.response.send_message(msg)
        
    @app_commands.command(name="toss", description="Tosses a coin")
    async def toss(self, ctx: discord.Interaction):
        flip = random.randint(1,2)
        if flip == 1: await ctx.response.send_message("**Heads**")
        else: await ctx.response.send_message("**Tails**")
        
    @app_commands.command(name="roll", description="Rolls a dice")
    async def roll(self, ctx: discord.Interaction):
        outcome = random.randint(1, 6)
        await ctx.response.send(f"Its a **{outcome}**")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))