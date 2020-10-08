#!/usr/bin/python3
import discord
import json
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = "Token" # Put your discord bot token here

def emojiToJson(link, name):
  with open('emoji.json', 'r') as json_file:
    emojiDict = json.load(json_file)
    json_file.close()

  if f"{name}" in emojiDict:
    return "Emoji Name Already Taken"

  emojiDict[name] = link

  with open('emoji.json', 'w') as json_file:
    json.dump(emojiDict, json_file)

  return f"Emoji {name} Created"

def deleteEmoji(name):
  with open('emoji.json', 'r') as json_file:
    emojiDict = json.load(json_file)
    json_file.close()

  if f"{name}" in emojiDict:
    emojiDict.pop(f"{name}")
    
  else:
    return "Emoji Dosen't exist"

  with open('emoji.json', 'w') as json_file:
    json.dump(emojiDict, json_file)

  return f"Emoji {name} deleted"

def listEmojis():
  with open('emoji.json', 'r') as json_file:
    emojiDict = json.load(json_file)
    json_file.close()

  emojiString = "Emojis\n"

  for key in emojiDict:
    emojiString += key+"\n"
    
  emojiString += "There are " + (str(len(emojiDict))) + "Emojis \n"

  print(emojiString)

  return emojiString

def getEmojiByName(name):
  with open('emoji.json', 'r') as json_file:
    emojiDict = json.load(json_file)
    json_file.close()

  if name in emojiDict:
    pass

  else:
    return "Emoji Does Not Exist"

  return emojiDict.get(name)

@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")

@bot.command(pass_context=True)
async def emoji(ctx, name):
  emoji = str(getEmojiByName(name))
  await ctx.send(emoji)

@bot.command(pass_context=True)
async def addEmoji(ctx, name, link):
  result = emojiToJson(link, name)
  await ctx.send(result)

@bot.command(pass_context=True)
async def listEmoji(ctx):
  stuff = listEmojis()
  result = "```" + stuff + "```"
  await ctx.send(result)

@bot.command(pass_contex=True)
async def delEmoji(ctx, name):
  result = deleteEmoji(name)
  await ctx.send(result)
 
bot.run(TOKEN)
