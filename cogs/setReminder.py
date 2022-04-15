from discord.ext import commands


class SetReminder(commands.Cog, name="SetReminder"):
    """Sets a reminder for a determined date."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='setreminder',
        description='de que precisas que eu te relembre?',
        guild_ids=[826008856714543134, 943609804528713779])
    async def setReminder(self, ctx):
        await ctx.respond("Esta funcionalidade ainda não foi implementada!")


def setup(bot: commands.Bot):
    bot.add_cog(SetReminder(bot))
