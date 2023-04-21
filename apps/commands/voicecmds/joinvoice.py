import nextcord
from nextcord.ext import commands


class joinvc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="join",
        description="Make the Bot join the VC",
        force_global=True
    )
    async def jvc(self, ctx: nextcord.Interaction):
        channel = nextcord.utils.get(ctx.guild.channels, id=743067601940512888)
        print("fetching audio file")
        print("connecting")
        await nextcord.VoiceClient(self.bot, channel).connect(
            reconnect=True,
            timeout=60.0
        )


def setup(bot):
    bot.add_cog(joinvc(bot))
