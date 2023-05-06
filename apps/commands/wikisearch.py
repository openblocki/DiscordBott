import nextcord
from nextcord.ext import commands
import wikipediaapi


class WikiSearcher(commands.Cog):

    WIKI_WIKI = wikipediaapi.Wikipedia('en')
    PAGE_PY = ""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="wikisearch",
        description="Knowledge for everyone. If title isn't exact, it might search for a maximum of 5 Articles",
        force_global=True
    )
    async def search_wiki(self, ctx: nextcord.Interaction, search: str):

        self.PAGE_PY = self.WIKI_WIKI.page(search)
        if self.PAGE_PY.exists():
            await ctx.send("`" +
                           self.PAGE_PY.title +
                           "`" +
                           "\n \n" +
                           self.PAGE_PY.summary[0:1500].replace(".", ".\n") +
                           "\n If you want to continue reading click this [[Click]](" +
                           self.PAGE_PY.fullurl +
                           ")"
                           )

        else:
            # await ctx.send(wp.search(search, results=5))
            await ctx.send("[] Error 404: Page not Found []")


def setup(bot):
    bot.add_cog(WikiSearcher(bot))
