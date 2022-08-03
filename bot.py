from ast import Await
import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "/", description = "crée par @ESPADON#9696")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def salut(ctx):
    print("salut")
    await ctx.send("salut salut l'ami !")

@bot.command()
async def infoserv(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"La population du serveur **{serverName}** s'élève à **{numberOfPerson}** personnes ! \nsa description est **{serverDescription}**. \nsur ce serveur il y a **{numberOfTextChannels}** salons text et **{numberOfVoiceChannels}** salon vocaux."
	await ctx.send(message)

@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à pris une giffle par la loi et s'est assagit donc il revient parmis nous !")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"Le citoyen {user} n'aparait pas dans la liste des bans")

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")

@bot.command()
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

@bot.command()
async def webhook(ctx):
	print("webhook")
	await ctx.send("**voici ton lien de fabrication d'annonce:** \nhttps://discohook.org/?data=eyJtZXNzYWdlcyI6W3siZGF0YSI6eyJjb250ZW50IjpudWxsLCJlbWJlZHMiOlt7ImNvbG9yIjozMDkyNzkwfV0sImF0dGFjaG1lbnRzIjpbXX19XX0")

bot.run("MTAwMTE3NzU3NzA0MzUzODA3MA.G7j10h.FbsJHenREQGB7Q1gJ2JzJ34k9mBRNmryKbJw1A")


