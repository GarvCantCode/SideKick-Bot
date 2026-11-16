import discord
from discord import app_commands
from discord.ext import commands


class Research(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="define", description="Returns defination for that word")
    async def define(self, ctx: discord.Interaction, word: str):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip().lower()}"

        async with self.bot.session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                msg = f"Definition for **{word}** is **{data[0]["meanings"][0]["definitions"][0]["definition"]}**"
                await ctx.response.send_message(msg)
            elif response.status == 404:
                await ctx.response.send_message(f"No defination found for **{word}**.")
            else:
                await ctx.response.send_message(f"Failed to fetch the defination for **{word}**.")

async def setup(bot):
    await bot.add_cog(Research(bot))