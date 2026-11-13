import random

import discord
from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.unicode = [chr(c) for c in range(0x0300, 0x0370)]
        
    def make_zalgo(self, text, intensity):
        zalgoed_text = []
        
        for i in text:
            zalgoed_text.append(i)
            zalgoed_text.append("".join(random.choices(self.unicode, k=random.randint(1, intensity))))
        
        return "".join(zalgoed_text) 
        
    @app_commands.command(name="zalgo", description="Make text look glitchy and cursed")
    async def zalgo(self, ctx: discord.Interaction, text: app_commands.Range[str, 1, 250], intensity: app_commands.Range[int, 1, 10]):
        msg = self.make_zalgo(text=text, intensity=intensity)
        await ctx.response.send_message(msg)
        
async def setup(bot):
    await bot.add_cog(Fun(bot))