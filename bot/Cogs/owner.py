import discord
from bot.config import Configuration
from discord import app_commands
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="reload", description="reload the desired cog")
    async def reload(self, ctx: discord.Interaction, cog: str, user: discord.Member):
        if user.id == int(Configuration.OWNER_ID):
            await ctx.response.defer()
            try:
                await self.bot.reload_extension(f"bot.cogs.{cog}")
                await ctx.followup.send(f"Cog **{cog}** reloaded successfully.")
            except:
                await ctx.followup.send("Failed to reload the cog")      
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
