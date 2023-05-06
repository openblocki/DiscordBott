import nextcord
from nextcord.ext import commands
from src.logging.logging import Logging


class Calculator(commands.Cog):
    RESULT = "NIL"
    BUFFER_MESSAGE = ""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="Calculate",
        description="A Calculator, reinventing Math",
        force_global=True
    )
    async def calculate(
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

        await Logging("Calculator", self.bot, ctx).log()

        match operator:
            case "add":
                self.RESULT = x + y
            case "subs":
                self.RESULT = x - y
            case "mult":
                self.RESULT = x * y
            case "div":
                self.RESULT = x / y

        await ctx.send(str(self.RESULT))
        self.RESULT = "Nil"


def setup(bot):
    bot.add_cog(Calculator(bot))
