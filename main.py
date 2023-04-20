import nextcord
from nextcord.ext import commands
import os
from config.token import tkn


class main(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all())
        # Remove built-in help command because trash
        self.remove_command("help")
        # Check so it started
        print("hallo")
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

        # start Bot
        self.run(tkn.token())


main()
