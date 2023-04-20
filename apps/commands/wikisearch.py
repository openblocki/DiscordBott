import nextcord
from nextcord.ext import commands
import wikipediaapi
import os

class wiki(commands.Cog):

    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = ""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="wikisearch",
        description="Knowledge for everyone. If title isn't exact, it will search for a maximum of 5 Articles",
        force_global=True
    )
    async def wik(self, ctx: nextcord.Interaction, search: str):

        self.page_py = self.wiki_wiki.page(search)
        if self.page_py.exists():
            await ctx.send("`" + self.page_py.title + "`" + "\n \n" + self.page_py.summary[0:1500].replace(".", ".\n") +
                           "\n If you want to continue reading click this [[Click]](" + self.page_py.fullurl + ")")
        else:
            # await ctx.send(wp.search(search, results=5))
            await ctx.send("[] Error 404: Page not Found []")


def setup(bot):
    bot.add_cog(wiki(bot))
