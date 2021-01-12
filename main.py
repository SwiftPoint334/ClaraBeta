import discord
from replit import db
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print("Build Succeeded.")

@client.command()
async def ping(ctx):
  await ctx.send("Pong!")
  print("A message has been sent.")

client.run("Nzk4NTYyMDUwODA0MTU0MzY4.X_203Q.lzdXznZ27-b3OjhAAqVTOBZSPf4")