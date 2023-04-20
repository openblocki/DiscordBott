import nextcord
from nextcord.ext import commands


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
    async def clc(self, ctx: nextcord.Interaction, operator: str, x: int, y: int):

        if operator == ("add" or "addition"):
            self.result = x + y
        elif operator == ("substract" or "substraction" or "subs"):
            self.result = x - y
        elif operator == ("mult" or "multiply" or "multiplication"):
            self.result = x * y
        elif operator == ("div" or "division" or "divide"):
            self.result = x / y
        else:
            self.buffermsg = "Uh oh, thoust haveth done goofed. : "

        await ctx.send(self.buffermsg + str(self.result))
        self.result = "Nil"
        self.buffermsg = ""


def setup(bot):
    bot.add_cog(calc(bot))
