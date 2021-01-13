import discord
from discord_slash import SlashCommand
from discord_slash import SlashCommandOptionType
from discord_slash.utils import manage_commands

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, auto_register=True)

guild_ids = [752693493675327528]

@client.event
async def on_ready():
  print("Build Succeeded.")

@slash.slash(name="ping", description="Displays the ping.",guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(content=f"Pong! ({client.latency*1000}ms)")

@slash.slash(name="echo", description="Echo's text back to you.", guild_ids=guild_ids, options=[manage_commands.create_option("string", "A random string.", SlashCommandOptionType.STRING, True)])
async def _echo(ctx, string):
    await ctx.send(content=string)

@slash.slash(name="announce", description="Makes an announcement.", guild_ids=guild_ids, options=[manage_commands.create_option("channel", "The channel you want to send the announcement to.", SlashCommandOptionType.CHANNEL, True), manage_commands.create_option("message", "your message", SlashCommandOptionType.STRING, True)])
async def _announce(ctx, channel, message):
  await channel.send(f"{message}")

@slash.slash(name="warn", description="Warns a user.", guild_ids=guild_ids, options=[manage_commands.create_option("user", "A member", SlashCommandOptionType.USER, True), manage_commands.create_option("reason", "The reason for the warn.", SlashCommandOptionType.STRING, True)])
async def _warn(ctx, user, reason):
  await ctx.send()

  



client.run("Nzk4NTYyMDUwODA0MTU0MzY4.X_203Q.lzdXznZ27-b3OjhAAqVTOBZSPf4")