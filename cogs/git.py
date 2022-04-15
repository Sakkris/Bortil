from os.path import exists
import validators
from discord.ext import commands
from discord.commands import Option
from main import guilds

git_dict = {}

if exists("admin/Git.txt"):
    with open('admin/Git.txt', 'r') as f:
        for line in f:
            data = line.split(" - ")
            git_dict[data[0]] = data[1].rstrip("\n")
else:
    with open('admin/Git.txt', 'w'):
        pass


class Git(commands.Cog, name="git"):
    """Manages the git slashCommands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='get_git',
        description='Precisas de um Git?',
        guild_ids=guilds)
    async def get_git(self, ctx,
                      git_user: Option(str, "Escolhe o utilizador", choices=[*git_dict])):
        await ctx.respond(f"Git link para o utilizador {git_user}: {git_dict[git_user]}")

    @commands.slash_command(
        name='add_git',
        description='Queres adicionar um Git?',
        guild_ids=guilds)
    async def add_git(self, ctx,
                      git_user: Option(str, "Qual o utilizador?"),
                      git_link: Option(str, "Qual o link?")):

        if not validators.url(git_link):
            await ctx.respond("Isso não é um link!")
            return

        if not git_link.startswith("https://github.com/"):
            await ctx.respond("Isso não é um link para o GitHub!")
            return

        file = open("admin/Git.txt", "a")
        file.write(f"{git_user} - {git_link}\n")
        file.close()

        git_dict[git_user] = git_link

        await ctx.respond(f"O Git link para o utilizador {git_user} foi adicionado! {git_link}")


def setup(bot: commands.Bot):
    bot.add_cog(Git(bot))
