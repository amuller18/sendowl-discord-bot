import discord
from discord.ext import commands
from discord.commands import Option
import requests
import json


bot = commands.Bot(prefix = commands.when_mentioned_or('!'))
token=''
url = 'https://cdbbe2bb52b6776:401309836a2ab4d8a93b@www.sendowl.com/api/v1/orders/'

@bot.event
async def on_ready():
    print(f"Bot loaded")


@bot.slash_command(description = 'Input order ID to get the emails and proxies the customer ordered.')
async def getorder(x, orderid:Option(str,"Enter order ID")):
    list = []
    print('Recieved request')
    print(x,'x')
    r = requests.get(url + str(orderid) + '/licenses', headers = {'Accept': 'application/json'})
    list = []
    r = requests.get(url + str(orderid) + '/licenses', headers = {'Accept': 'application/json'})
    text = json.loads(r.text)
    for d in text:
        getkey = d.get('license')
        key = getkey.get('key')
        orderid = getkey.get('order_id')
        list.append(key)
    message = 'Order ID' +  str(orderid) + ' contains the following One Clicks: '
    await x.send(message)
    for d in list:
        await x.send(d)
        print(d)
        
zzz = True
while zzz == True:
    bot.run(token)
