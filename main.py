import nextcord
from nextcord.ext import commands
import os
from config.token import tkn
from nextcord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


class main(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all())
        # Remove built-in help command because trash
        self.remove_command("help")
        # Check so it started
        print("hallo")

        for opus_lib in OPUS_LIBS:
            try:
                opus.load_opus(opus_lib)
            except OSError:
                pass

        # Get the cogs
        for root, dirs, files in os.walk("apps"):
            for name in files:
                if str(root).endswith("__pycache__"):
                    continue
                self.load_extension(os.path.join(root, name).replace("/", ".")[:-3])

        @self.event
        async def on_ready():
            print(f'We have logged in as {self.user}')
            channel = self.get_channel(743067601437065221)
            await channel.send("I have arrived [not nutted]")
            await channel.send("Opus Loaded: " + str(opus.is_loaded()))

        # @self.event
        # async def on_interaction(ctx: nextcord.Interaction) -> None:
        #     chl = self.get_channel(1100427923787362334)
        #     await chl.send(str(ctx))

        # start Bot
        self.run(tkn.token())


main()
