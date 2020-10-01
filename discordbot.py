from discord.ext import commands
import os
import discord
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_command_error(ctx, error):

bot.run(token)
