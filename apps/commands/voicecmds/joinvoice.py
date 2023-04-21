import nextcord
from nextcord.ext import commands
import asyncio

class joinvc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="join",
        description="Make the Bot join the VC",
        force_global=True
    )
    async def jvc(self, ctx: nextcord.Interaction):
        voice_channel = ctx.user.voice.channel
        voice_client: nextcord.VoiceClient = await voice_channel.connect()
        audio_file = nextcord.FFmpegPCMAudio("mats/sounds/mpfall.mp3")
        if not voice_client.is_playing():
            voice_client.play(audio_file)
            await ctx.send("Playing...")
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()
        else:
            await ctx.send("Stop, you're violating time and space")


def setup(bot):
    bot.add_cog(joinvc(bot))
