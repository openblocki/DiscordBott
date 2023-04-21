import nextcord
from nextcord.ext import commands


class playsnd(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="ply",
        description="Its to test things ja fucking knobhead, what did you expect",
        force_global=True
    )
    async def pls(self, ctx: nextcord.Interaction):
        asource = nextcord.FFmpegPCMAudio("mats/sounds/mpfall.mp3")
        channel = nextcord.utils.get(ctx.guild.channels, id=743067601940512888)
        print("trying to play")
        nextcord.VoiceClient(self.bot, channel).play(source=asource, after=lambda: print("played audio"))
        print("played")
        await ctx.send("done")


def setup(bot):
    bot.add_cog(playsnd(bot))
