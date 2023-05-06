import nextcord
from nextcord.ext import commands


class Stop(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="stop",
        description="Stop the Bot, stop it before it lays eggs",
        force_global=True
    )
    @commands.is_owner()
    async def stp(self, ctx: nextcord.Interaction):
        await ctx.send("ok")
        exit()


def setup(bot):
    bot.add_cog(Stop(bot))
