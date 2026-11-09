"""Bots main processes: startup, cogs load"""

import platform
from pathlib import Path

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

COGS_DIR = Path(__file__).resolve().parent / "Cogs"
COGS_PACKAGE = f"{__package__}.Cogs"

class Sidekicktree(app_commands.CommandTree):
    def __init__(self, client):
        super().__init__(
            client,
            allowed_contexts=app_commands.AppCommandContext(guild=True, dm_channel=True, private_channel=True),
            allowed_installs=app_commands.AppInstallationType(guild=False, user=True)
            )
    
class core(commands.Bot):
    def __init__(self, settings, logger):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents =discord.Intents.default(),
            help_command=None,
            tree_cls=Sidekicktree,
            owner_id=settings["owner_id"], # owner-id
            activity =discord.Game("in your room") #status - edit it however you want
            )
        
        self.settings = settings
        self.logger = logger
        self.session = None
        
    async def load_cogs(self) -> None:
        for i in COGS_DIR.glob("*.py"):
            if i.name.startswith("_"):
                continue
                
            extention = f"{COGS_PACKAGE}.{i.stem}"
            if extention in self.extensions:
                continue
            
            try:
                await self.load_extension(extention)
                self.logger.info(f"Loaded extention '{extention}'")
            except commands.ExtensionError as e:
                exception = f"{type(e).__name__}: {e}"
                self.logger.exception(
                    f"Failed to load extention {extention}\n{exception}"
                )

    async def setup_hook(self):
        self.logger.info(f"Discord.py: {discord.__version__} Python Version: {platform.python_version()}")
        self.session= aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15))
        
        await self.load_cogs()
        
        if self.settings["sync_on_start"] == True:
            sync = await self.tree.sync()
            self.logger.info(f"Sync: {len(sync)}")
            
    async def on_ready(self):
        self.logger.info(f"Ready as: {self.user} ID: {self.user.id}")
        
    async def close(self):
        if self.session is not None and not self.session.closed:
            await self.session.close()

        await super().close()