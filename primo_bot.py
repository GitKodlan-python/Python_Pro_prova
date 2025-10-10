import discord, random, os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def gen_emodji(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send(random.choice(emodji))

@bot.command()
async def password(ctx, lenght= int):
    caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    genera_password= " "
    for i in range(lenght):
        genera_password += random.choice(caratteri)
    await ctx.send(genera_password)


@bot.command()
async def leggi(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        #print(f.read())
        await ctx.send(f.read())

@bot.command()
async def scrivi(ctx):
    with open('text.txt', 'w', encoding='utf-8') as f:
        text = "ciao a tutti! oggi programmo il mio bot"
        f.write(text)


@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("metti il token")
