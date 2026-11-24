import discord
from discord import app_commands
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="reload", description="Reload the desired cog")
    async def reload(self, ctx: discord.Interaction, cog: str):
        if not await self.bot.is_owner(ctx.user):
            await ctx.response.send_message("Owner only.", ephemeral=True)
            return

        await ctx.response.defer(ephemeral=True)
        try:
            await self.bot.reload_extension(f"src.cogs.{cog}")
        except commands.ExtensionError as error:
            await ctx.followup.send(f"Failed to reload **{cog}**: {error}", ephemeral=True)
            return
        await ctx.followup.send(f"Cog **{cog}** reloaded successfully.", ephemeral=True)
                
async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
