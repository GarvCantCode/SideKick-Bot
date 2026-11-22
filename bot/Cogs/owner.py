import discord
from discord import app_commands
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="reload", description="reload the desired cog")
    @commands.is_owner()
    async def reload(self, ctx: discord.Interaction, cog: str):
        await ctx.response.defer()
        
        await self.bot.reload_extension(f"bot.cogs.{cog}")
        await ctx.followup.send(f"Cog **{cog}** reloaded successfully.")
                
async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
