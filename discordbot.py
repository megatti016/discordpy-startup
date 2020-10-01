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
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

async def on_member_join(member):
CHANNEL_ID = '699621884643377194'
    channel = bot.get_channel(CHANNEL_ID)
    infomation_ch = bot.get_channel('699621884643377194')
    zikosyoukai_ch = bot.get_channel('699621884643377194')
    
bot.run(token)
