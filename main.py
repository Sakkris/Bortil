import sys
import traceback
import discord
import os


bot = discord.Bot()
with open('admin/Token.txt') as f:
    token = f.readline()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


def main():
    for cog_file in os.listdir("cogs"):
        if not cog_file.startswith('_'):
            cog = "cogs." + cog_file.split(".")[0]

            try:
                bot.load_extension(cog)
            except Exception as e:
                print(f'Failed to load extension {cog}.', file=sys.stderr)
                traceback.print_exc()

    bot.run(token)


if __name__ == '__main__':
    main()
