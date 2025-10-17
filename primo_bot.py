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
async def inquinamento2(ctx):
    with open('text_inquinamento.txt', 'r', encoding='utf-8') as f:
        #print(f.read())
        await ctx.send(f.read())

@bot.command()
async def inquinamento(ctx):
    curiosita = ["l'inquinamento  non fa bene alla terra", "l'inquinamento che produciamo ci danneggia"]
    await ctx.send(random.choice(curiosita))

@bot.command()
async def mem(ctx):
    with open('meme/mem1.png', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open(f'meme/mem2.png', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open(f'meme/mem3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem4(ctx):
    with open(f'meme/mem4.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem5(ctx):
    with open(f'meme/mem5.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem6(ctx):
    with open(f'meme/mem6.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem7(ctx):
    with open(f'meme/mem7.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem8(ctx):
    with open(f'meme/mem8.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def inquinamento_fa_male(ctx):
    await ctx.send(f'si fa male, quindi NON FARE INQUINAMENTO!!!')

bot.run("metti il token")
