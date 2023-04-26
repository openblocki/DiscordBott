from nextcord import Message
from nextcord.ext import commands
import nextcord

class Logging:
    def __init__(self, cmd_name: str, bot: commands.Bot, ctx: nextcord.Interaction):
        self.cmd_name = cmd_name
        self.bot = bot
        self.ctx = ctx

    async def log(self) -> Message:
        channel = self.bot.get_channel(1100427923787362334)
        return await channel.send(f"{self.cmd_name} got executed by {self.ctx.user}.")
