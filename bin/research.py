import discord
from discord import app_commands
from discord.ext import commands


class Research(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="define", description="Returns defination for that word")
    async def define(self, ctx: discord.Interaction, word: str):
        await ctx.response.defer()
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip().lower()}"

        async with self.bot.session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                msg = f"Definition for **{word}** is **{data[0]["meanings"][0]["definitions"][0]["definition"]}**"
                await ctx.followup.send(msg)
            elif response.status == 404:
                await ctx.followup.send(f"No defination found for **{word}**.")
            else:
                await ctx.followup.send(f"Failed to fetch the defination for **{word}**.")
                
    @app_commands.command(name="weather", description="Returns weather condition for that city")
    async def weather(self, ctx:discord.Interaction, city: str):
        await ctx.response.defer()
        geo_code = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
        
        async with self.bot.session.get(geo_code) as response:
            if response.status != 200:
                await ctx.followup.send(f"Failed to fetch coordinates for **{city}**")
                return
                
            data = await response.json()
            
            if not data.get('results'):
                await ctx.followup.send(f"Noo city found: **{city}**")
                return
                
            coordinates = data['results'][0]
            
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates['latitude']}&longitude={coordinates['longitude']}&current=temperature_2m,apparent_temperature&timezone=auto"
        
        async with self.bot.session.get(url) as resp:
            if resp.status != 200:
                await ctx.followup.send(f"Failed to fetch weather for **{city}**") 
                return
            
            data_weather = await resp.json()

            msg = (
                f"**{city}** weather\n"
                f"Temperature: **{data_weather['current']['temperature_2m']}°C**\n"
                f"Feels like: **{data_weather['current']['apparent_temperature']}°C**"
            )

            await ctx.followup.send(msg)

async def setup(bot):
    await bot.add_cog(Research(bot))