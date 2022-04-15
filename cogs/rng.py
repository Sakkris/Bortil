from discord.ext import commands
from discord.commands import Option
from main import guilds

import random


class RNG(commands.Cog, name="rng"):
    """Chooses a random number from a given range."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='rng',
        description='Queres que escolha um número à sorte?',
        guild_ids=guilds)
    async def rng(self, ctx,
                  higher_lim: Option(int, "Limite Superior"),
                  lower_lim: Option(int, "Limite Inferior [Default: 0]", default=0, required=False)):
        await ctx.respond(f"Escolhi um número aleatório entre {lower_lim} e {higher_lim} -> "
                          f"{random.randrange(lower_lim, higher_lim)}")


def setup(bot: commands.Bot):
    bot.add_cog(RNG(bot))
