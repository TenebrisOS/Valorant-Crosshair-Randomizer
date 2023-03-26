import discord
import time
import json
import io
#from discord import app_commands
import interactions
#from discord.ext import commands
#from discord_slash import commands, SlashCommand, SlashContext
import asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pyvirtualdisplay import Display 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from discord import ButtonStyle, ActionRow, Button
#from discord import SlashCommand
import os
from discord.ext import commands
from discord import Color
import pyperclip

with open('C:/Users/modib/Documents/kali/py/ValRandomCrosshair/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
#tree = app_commands.CommandTree(client)
PREFIX = ";"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
options = Options()
driver = webdriver.Chrome(options=options)
#endregion

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Your privates mess ;)"))

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]
    print(args)
    if args[0] == "Generate" :
        driver.get('https://www.vcrdb.net/builder?c=0')
        randomizerButton = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="builderRandomize"]'))
        randomizerButton.click()
        copyButton = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="builderCopy"]'))
        img = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="builderImage"]/div[1]/x-hair/canvas'))
        imgPATH = 'C:/Users/modib/Documents/kali/py/ValRandomCrosshair/img.png'
        img.screenshot(imgPATH)
        copyButton.click()
        code = pyperclip.paste()
        mbd = discord.Embed(title="Crosshair :", color = Color.green())
        #mbd.set_image(url = discord.File(imgPATH))
        mbd.add_field(name = "Here is your random code", value = ('`' + code + '`'))
        pyperclip.copy('')
        await message.channel.send(embed = mbd)
        await message.channel.send(file = discord.File(imgPATH))
        os.remove(imgPATH)

client.run(TOKEN)