from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =757346851963011172  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758285489257054238/xjpsupergirls_ani05ban.gif') 

    if now == '01:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758286779920285747/xjpsupergirls_ani07ban.gif') 

    if now == '02:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/741585316703633419/758286759716323328/xjpsupergirls_ani06ban.gif')
        
    if now == '03:04':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757745371765145630/xjpsupergirls_ani00ban.gif')
        
    if now == '04:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757759865044074536/xjpsupergirls_ani04ban.gif') 
        
    if now == '05:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757759856789815356/xjpsupergirls_ani03ban.gif') 
        
    if now == '06:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757759841237205103/xjpsupergirls_ani02ban.gif') 
        
    if now == '08:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757745371765145630/xjpsupergirls_ani00ban.gif')
        
    if now == '09:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757458033533124649/XJPGIRL00.png')
   
    if now == '11:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757458053707726880/XJPGIRL02.png') 
 
    if now == '12:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/757159787996905552/xjpimage02.gif') 

    if now == '13:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758668048613507102/xjpgirls2.png') 
        
    if now == '14:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758655911841103892/xjpgirls1.png') 
        
    if now == '16:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758286759716323328/xjpsupergirls_ani06ban.gif') 
    
    if now == '20:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/758285489257054238/xjpsupergirls_ani05ban.gif')
        
#ループ処理実行
loop.start()


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "<:xjpsupergirls_02:757807252496318535> <:xjpsupergirls_02:757807252496318535> <:xjpsupergirls_02:757807252496318535>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:xjpsupergirls_01:757806007475896441> <:xjpsupergirls_01:757806007475896441> <:xjpsupergirls_01:757806007475896441>")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "<:xjpsupergirls_01:757806007475896441> <:xjpsupergirls_01:757806007475896441> <:xjpsupergirls_01:757806007475896441>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:xjpsupergirls_02:757807252496318535> <:xjpsupergirls_02:757807252496318535> <:xjpsupergirls_02:757807252496318535>")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "ThankYou!!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💛{message.author.mention} 💛 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "Thank U":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💚 {message.author.mention} 💚 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "Thank you everybody":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💙 {message.author.mention} 💙 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "g.morning":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear♥ {message.author.mention}♥. good Morning🌞")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "Good day all":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear♥ {message.author.mention}♥. Thank YOU! Good luck🌟 ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:xjp_coin:739313946045055117> <:xjp_coin:739313946045055117> <:xjp_coin:739313946045055117>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:gf:721588114283298908> 💚{message.author.mention}さん💚 <:xjp_coin:739313946045055117> <:xjpsupergirls_02:757807252496318535> <:xjpsupergirls_01:757806007475896441>")  # f文字列（フォーマット済み文字列リテラル）
  
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/r":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$deposit")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/bal":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$bal")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 


# Botの起動とDiscordサーバーへの接続
client.run(token)

