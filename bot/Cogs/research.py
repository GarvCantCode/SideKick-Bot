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
                
    @app_commands.command(name="weather", description="Returns weather condition for that city")
    async def weather(self, ctx:discord.Interaction, city: str):
        geo_code = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
        
        async with self.bot.session.get(geo_code) as response:
            if response.status == 200:
                data = await response.json()
                coordinates = data['results'][0]
                url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates['latitude']}&longitude={coordinates['longitude']}&current=temperature_2m,apparent_temperature&timezone=auto"
                async with self.bot.session.get(url) as resp:
                    if resp.status == 200:
                        data_weather = await resp.json()
                        msg = f"{city}: **{data_weather['current']['temperature_2m']}**°C, feels like **{data_weather['current']['apparent_temperature']}°C**"
                        await ctx.response.send_message(msg)
                    elif resp.status == 404:
                        await ctx.response.send_message(f"No information found for **{city}**.")
                    else:
                        await ctx.response.send_message(f"Failed to fetch the information for **{city}**.")
            elif response.status == 404:
                await ctx.response.send_message(f"No city found: **{city}**.")
            else:
                await ctx.response.send_message(f"Failed to fetch the coordinates for **{city}**.")

async def setup(bot):
    await bot.add_cog(Research(bot))