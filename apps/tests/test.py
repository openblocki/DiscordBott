import nextcord
from nextcord.ext import commands


class test(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="tst",
        description="Its to test things ja fucking knobhead, what did you expect",
        force_global=True
    )
    async def tst(self, ctx: nextcord.Interaction):
        channel = nextcord.utils.get(ctx.guild.channels, id=743067601940512888)
        await ctx.send(str(nextcord.VoiceClient(self.bot, channel).is_connected()))
        await ctx.send("test")


def setup(bot):
    bot.add_cog(test(bot))
