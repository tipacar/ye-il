import discord

from discord.ext import commands
from bot_token import token
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def cevre(ctx):
    with open('m2l1/images/poset.jpeg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture1 = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    
    with open('m2l1/images/araba.jpeg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture2 = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    with open('m2l1/images/kutu.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture3 = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send('alışverişte plastik poşet kullanmak yerine kumaş poşet kullana bilirsin.')
    await ctx.send(file=picture1)
    await ctx.send('benzinli araba kullanmak yerine elektrikli araba kullanabilirsin.')
    await ctx.send(file=picture2)
    await ctx.send('etrafa çöp atmayabilirsin.')
    await ctx.send(file=picture3)
bot.run(token)