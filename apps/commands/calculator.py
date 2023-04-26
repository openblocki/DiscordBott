import nextcord
from nextcord.ext import commands
from src.logging.logging import Logging


class calc(commands.Cog):
    result = "Nil"
    buffermsg = ""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="calc",
        description="A Calculator, reinventing Math",
        force_global=True
    )
    async def clc(
            self,
            ctx: nextcord.Interaction,
            operator: str = nextcord.SlashOption(
                description="Select Operator",
                choices={"add": "add", "subs": "subs", "mult": "mult", "div": "div"}
            ),
            x: int = nextcord.SlashOption(
                description="Select First"
            ),
            y: int = nextcord.SlashOption(
                description="Select Second"
            )
    ) -> None:

        await Logging("Calc", self.bot, ctx).log()

        match operator:
            case "add":
                self.result = x + y
            case "subs":
                self.result = x - y
            case "mult":
                self.result = x * y
            case "div":
                self.result = x / y

        await ctx.send(str(self.result))
        self.result = "Nil"


def setup(bot):
    bot.add_cog(calc(bot))
