import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='~u ')
client = discord.Client()

@bot.event
async def on_ready():
    print('Unicorn is Ready')

@bot.event
async def on_member_join(member):
    print(f"{member} has joined the server")


@bot.event
async def on_member_remove(member):
    print(f"{member} has left the server")



@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

@bot.command()
async def avocado():
    print("I don't want those.")

# Main Script
bot.run('NDI4MzY3MjA5OTQ2MTUyOTYw.WrryDQ.zwRfcfCi_VEKF3GAptTejZQzNGo')