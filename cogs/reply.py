from discord.ext import commands
from random import randrange


class Reply(commands.Cog, name="Reply"):
    """Replies to messages written in the chat"""

    wisdomMessages = [
        'ainda vais a tempo de desistir do curso',
        'se hackeares o ISEP, n deixes rasto...',
        'isto n é o secundário, tens de ser autonomo, arranja a tua própria wisdom',
        ':face_exhaling:',
        'n',
        'procura nos slides',
    ]

    reactions = [
        ':smirk:',
        ':smile:',
        ':smiling_face_with_3_hearts:',
        ':triumph:',
        ':flushed:',
        ':yawning_face:',
        ':rolling_eyes:',
        ':clown:'
    ]

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower() == 'bom dia bortil':
            await message.reply('Bom dia {}'.format(self.reactions[randrange(len(self.reactions) - 1)]),
                                mention_author=True)

        if message.content.lower() == "boa noite bortil":
            await message.reply('Boa noite {}'.format(self.reactions[randrange(len(self.reactions) - 1)]),
                                mention_author=True)

        if message.content.lower() == 'bortil give me your wisdom pls':
            await message.reply(self.wisdomMessages[randrange(len(self.wisdomMessages) - 1)],
                                mention_author=True)


def setup(bot: commands.Bot):
    bot.add_cog(Reply(bot))
