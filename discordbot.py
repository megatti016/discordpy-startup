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
async def on_member_join(member):
   CHANNEL_ID = 699621884643377194
    channel = bot.get_channel(CHANNEL_ID)
    infomation_ch = bot.get_channel(699621884643377194)
    zikosyoukai_ch = bot.get_channel(699621884643377194)
    await channel.send(str(member.mention)+'音MAD作者プリコネサーバー へようこそ！\n'+str(infomation_ch.mention)+ 'をご一読ください\n' + str(zikosyoukai_ch.mention)+ 'で音MAD作者とわかるようなURLと軽い自己紹介をよろしくお願いします\n※このチャンネルの通知をオフにすることを推奨します')
  

bot.run(token)
