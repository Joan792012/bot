import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'Conexion exitosa hemos iniciado sesion como {bot.user}')

@bot.command()
async def Hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def jaja(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)

bot.run("tu token de bot va aqui")
