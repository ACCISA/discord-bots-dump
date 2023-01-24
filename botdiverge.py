import discord
import threading
import socket
from time import perf_counter
import random
import aiofiles
import os.path
import asyncio
from asyncio import sleep
import sqlite3
from dotenv import load_dotenv
# import discord-components
import discord_components
# from discord_buttons import *
from discord_components import *
from discord_components.client import DiscordComponents
import csv
import pymysql
import valve.source
import valve.source.a2s
import valve.source.master_server
import a2s
import pandas
from sys import exit

from datetime import date
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import pandas as pd
from random import randint
from discord.ext import commands, tasks
# import pyodbc (module does not exist)

token = 'OTI4Mzg3NzQ4MDUyNzI5OTQ3.YdYCdw.y1I85Rl5SLWsPapZJAH1J1R-ouA'
today = date.today()
week = today.weekday()
hour = datetime.today().time()
openHour = hour.replace(hour=14,minute=30,second=0,microsecond=0)
closeHour = hour.replace(hour=21,minute=0,second=0,microsecond=0)

load_dotenv()
client = commands.Bot(command_prefix = '.', help_command=None)
client.remove_command('help')
clients = discord.Client(activity=discord.Game(name='my game'))
activity = discord.Activity(name='The Empire Grow', type=discord.ActivityType.watching)
clients = discord.Client(activity=activity)



#gspread
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

stock_data = client1.open('[DV-N] Stock Market').sheet1
stock_list = client1.open('[DV-N] Stock Market').get_worksheet(1)
stock_logs = client1.open('[DV-N] Stock Market').get_worksheet(2)
stock_name = client1.open('[DV-N] Stock Market').get_worksheet(3)
stock_sale = client1.open('[DV-N] Stock Market').get_worksheet(4)
stock_refe = client1.open('[DV-N] Stock Market').get_worksheet(5)
stock_brok = client1.open('[DV-N] Stock Market').get_worksheet(6)
#gspread
# async def sendMes():
#     threading.Timer(5.0, sendMes).start()
#     channel = client.get_channel(928471767440310325)
#     await channel.send('test')





@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name="The Stock Market"
    ))
    # DiscordComponents(client, change_discord_methods=True)

    print('Bot is online.')
    DiscordComponents(client)
    # batch_1_update.start()
    # batch_2_update.start()
    # batch_3_update.start()
    # batch_4_update.start()
    batch_update.start()


@tasks.loop(seconds=10)
async def batch_update():
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

    colorList = [default, teal,dark_teal,green,dark_green,blue,dark_blue,purple,dark_purple,magenta,dark_magenta,gold,dark_gold,orange,dark_orange,red,dark_red,lighter_grey,dark_grey,light_grey,darker_grey,blurple,greyple]
    randColor = random.choice(colorList)

    allGet = stock_list.batch_get(['B2:B2','B3:B3','B4:B4','B5:B5','B6:B6','C2:C2','C3:C3','C4:C4','C5:C5','C6:C6','E2:E2','E3:E3','E4:E4','E5:E5','E6:E6','F2:F2','F3:F3','F4:F4','F5:F5','F6:F6','H2:H2','H3:H3','H4:H4','H5:H5','H6:H6','B7:B7','B8:B8','B9:B9','B10:B10','B11:B11','C7:C7','C8:C8','C9:C9','C10:C10','C11:C11','E7:E7','E8:E8','E9:E9','E10:E10','E11:E11','F7:F7','F8:F8','F9:F9','F10:F10','F11:F11','H7:H7','H8:H8','H9:H9','H10:H10','H11:H11','B12:B12','B13:B13','B14:B14','B15:B15','B16:B16','C12:C12','C13:C13','C14:C14','C15:C15','C16:C16','E12:E12','E13:E13','E14:E14','E15:E15','E16:E16','F12:F12','F13:F13','F14:F14','F15:F15','F16:F16','H12:H12','H13:H13','H14:H14','H15:H15','H16:H16','B17:B17','B18:B18','B19:B19','B20:B20','B21:B21','C17:C17','C18:C18','C19:C19','C20:C20','C21:C21','E17:E17','E18:E18','E19:E19','E20:E20','E21:E21','F17:F17','F18:F18','F19:F19','F20:F20','F21:F21','H17:H17','H18:H18','H19:H19','H20:H20','H21:H21'])
    embed1 = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'View the stock market in real time.',
        colour = randColor
    )
    for x in range(5):
        embed1.add_field(name= allGet[20+x][0][0], value = '-------------------', inline = False)
        embed1.add_field(name= 'Current Price', value = allGet[x][0][0], inline = True)
        embed1.add_field(name= 'Percent Change', value = allGet[5+x][0][0], inline = True)
        embed1.add_field(name= 'Highest Price', value = allGet[10+x][0][0], inline = False)
        embed1.add_field(name= '====================================', value = '====================================', inline = False)
    channel = client.get_channel(929174615501201479)
    msg = await channel.fetch_message(929178758408175617)
    await asyncio.sleep(1)
    await msg.edit(embed = embed1)
#----------------------------------------
    embed2 = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'View the stock market in real time.',
        colour = randColor
    )
    for x in range(5):
        embed2.add_field(name= allGet[25+20+x][0][0], value = '-------------------', inline = False)
        embed2.add_field(name= 'Current Price', value = allGet[25+x][0][0], inline = True)
        embed2.add_field(name= 'Percent Change', value = allGet[25+5+x][0][0], inline = True)
        embed2.add_field(name= 'Highest Price', value = allGet[25+10+x][0][0], inline = False)
        embed2.add_field(name= '====================================', value = '====================================', inline = False)
    channel = client.get_channel(929174615501201479)
    msg = await channel.fetch_message(929178778201112636)
    await asyncio.sleep(1)
    await msg.edit(embed = embed2)
#----------------------------------------
    embed3 = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'View the stock market in real time.',
        colour = randColor
    )
    for x in range(5):
        embed3.add_field(name= allGet[50+20+x][0][0], value = '-------------------', inline = False)
        embed3.add_field(name= 'Current Price', value = allGet[50+x][0][0], inline = True)
        embed3.add_field(name= 'Percent Change', value = allGet[50+5+x][0][0], inline = True)
        embed3.add_field(name= 'Highest Price', value = allGet[50+10+x][0][0], inline = False)
        embed3.add_field(name= '====================================', value = '====================================', inline = False)
    channel = client.get_channel(929174615501201479)
    msg = await channel.fetch_message(931696233234452520)
    await asyncio.sleep(1)
    await msg.edit(embed = embed3)
#----------------------------------------
    embed4 = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'View the stock market in real time.',
        colour = randColor
    )
    for x in range(5):
        embed4.add_field(name= allGet[75+20+x][0][0], value = '-------------------', inline = False)
        embed4.add_field(name= 'Current Price', value = allGet[75+x][0][0], inline = True)
        embed4.add_field(name= 'Percent Change', value = allGet[75+5+x][0][0], inline = True)
        embed4.add_field(name= 'Highest Price', value = allGet[75+10+x][0][0], inline = False)
        embed4.add_field(name= '====================================', value = '====================================', inline = False)
    channel = client.get_channel(929174615501201479)
    msg = await channel.fetch_message(931696270005899265)
    await asyncio.sleep(1)
    await msg.edit(embed = embed4)
    print('Data Updated')
@client.command()
async def batch1(ctx):

    priceGet = stock_list.batch_get(['B2:B2','B3:B3','B4:B4','B5:B5','B6:B6','B7:B7','B8:B8','B9:B9','B10:B10','B11:B11'])
    percentGet = stock_list.batch_get(['C2:C2','C3:C3','C4:C4','C5:C5','C6:C6','C7:C7','C8:C8','C9:C9','C10:C10','C11:C11'])
    highGet = stock_list.batch_get(['E2:E2','E3:E3','E4:E4','E5:E5','E6:E6','E7:E7','E8:E8','E9:E9','E10:E10','E11:E11'])
    lowGet = stock_list.batch_get(['F2:F2','F3:F3','F4:F4','F5:F5','F6:F6','F7:F7','F8:F8','F9:F9','F10:F10','F11:F11'])
    nameGet = stock_list.batch_get(['H2:H2','H3:H3','H4:H4','H5:H5','H6:H6','H7:H7','H8:H8','H9:H9','H10:H10','H11:H11'])
    embed = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'View the stock market in real time.'
    )
    for i in range(len(priceGet)):
        embed.add_field(name=nameGet[i][0][0], value='-------------------',inline = False)
        embed.add_field(name='Current Price', value = priceGet[i][0][0],inline = True)
        embed.add_field(name='Percent Change', value = percentGet[i][0][0], inline = True)
        embed.add_field(name='Highest Price', value = highGet[i][0][0], inline = False)
        embed.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed)
    stock_logs.update('A1', '1')

@client.command()
async def batch2(ctx):

    priceGet = stock_list.batch_get(['B7:B7','B8:B8','B9:B9','B10:B10','B11:B11'])
    percentGet = stock_list.batch_get(['C7:C7','C8:C8','C9:C9','C10:C10','C11:C11'])
    highGet = stock_list.batch_get(['E7:E7','E8:E8','E9:E9','E10:E10','E11:E11'])
    lowGet = stock_list.batch_get(['F7:F7','F8:F8','F9:F9','F10:F10','F11:F11'])
    nameGet = stock_list.batch_get(['H7:H7','H8:H8','H9:H9','H10:H10','H11:H11'])
    embed = discord.Embed(
    title = 'Live Stock Viewer',
    description = 'View the stock market in real time.'
    )
    for i in range(len(priceGet)):
        embed.add_field(name=nameGet[i][0][0], value='-------------------',inline = False)
        embed.add_field(name='Current Price', value = priceGet[i][0][0],inline = True)
        embed.add_field(name='Percent Change', value = percentGet[i][0][0], inline = True)
        embed.add_field(name='Highest Price', value = highGet[i][0][0], inline = False)
        embed.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed)
    stock_logs.update('A2', '1')

@client.command()
async def batch3(ctx):

    priceGet = stock_list.batch_get(['B12:B12','B13:B13','B14:B14','B15:B15','B16:B16'])
    percentGet = stock_list.batch_get(['C12:C12','C13:C13','C14:C14','C15:C15','C16:C16'])
    highGet = stock_list.batch_get(['E12:E12','E13:E13','E14:E14','E15:E15','E16:E16'])
    lowGet = stock_list.batch_get(['F12:F12','F13:F13','F14:F14','F15:F15','F16:F16'])
    nameGet = stock_list.batch_get(['H12:H12','H13:H13','H14:H14','H15:H15','H16:H16'])
    embed = discord.Embed(
    title = 'Live Stock Viewer',
    description = 'View the stock market in real time.'
    )
    for i in range(len(priceGet)):
        embed.add_field(name=nameGet[i][0][0], value='-------------------',inline = False)
        embed.add_field(name='Current Price', value = priceGet[i][0][0],inline = True)
        embed.add_field(name='Percent Change', value = percentGet[i][0][0], inline = True)
        embed.add_field(name='Highest Price', value = highGet[i][0][0], inline = False)
        embed.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed)
    stock_logs.update('C1', '1')

@client.command()
async def batch4(ctx):

    priceGet = stock_list.batch_get(['B17:B17','B18:B18','B19:B19','B20:B20','B21:B21'])
    percentGet = stock_list.batch_get(['C17:C17','C18:C18','C19:C19','C20:C20','C21:C21'])
    highGet = stock_list.batch_get(['E17:E17','E18:E18','E19:E19','E20:E20','E21:E21'])
    lowGet = stock_list.batch_get(['F17:F17','F18:F18','F19:F19','F20:F20','F21:F21'])
    nameGet = stock_list.batch_get(['H17:H17','H18:H18','H19:H19','H20:H20','H21:H21'])

    embed = discord.Embed(
    title = 'Live Stock Viewer',
    description = 'View the stock market in real time.'
    )
    for i in range(len(priceGet)):
        embed.add_field(name=nameGet[i][0][0], value='-------------------',inline = False)
        embed.add_field(name='Current Price', value = priceGet[i][0][0],inline = True)
        embed.add_field(name='Percent Change', value = percentGet[i][0][0], inline = True)
        embed.add_field(name='Highest Price', value = highGet[i][0][0], inline = False)
        embed.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed)
    stock_logs.update('D1', '1')

async def respond(ctx ,message):
    embed = discord.Embed(
    title = message
    )
    await ctx.send(embed = embed)

async def respond(ctx ,message):
    embed = discord.Embed(
    title = message
    )
    await ctx.send(embed = embed)

async def registerCheck(ctx):
    author = ctx.message.author.id
    findID = stock_name.find(str(author))
    if findID == None:
        embed_reg = discord.Embed(
            title = 'ERROR',
            description = 'User is not registered.'
        )
        await ctx.send(embed = embed_reg)
        return False
    if findID != None:
        return

@client.command()
async def refresh(ctx):
    ripBozo.start()
    await respond(ctx, 'Refresh Started')

@client.command()
async def read(ctx):
    reading = stock_list.acell('D2').value
    await ctx.send(reading)

@client.command()
async def market(ctx, par=None):
    embed_update = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'All available stocks can be viewd here in real time',
    )

    googlePrice = stock_list.acell('B2').value
    googleShares = stock_list.acell('D2').value
    googlePercent = stock_list.acell('C2').value

    amazonPrice = stock_list.acell('B3').value
    amazonShares = stock_list.acell('D3').value
    amazonPercent = stock_list.acell('C3').value

    embed_update.add_field(name = 'Google', value = '------------------', inline = False)
    embed_update.add_field(name = 'Current Price' , value = googlePrice, inline = True)
    embed_update.add_field(name = 'Current Shares', value = googleShares, inline = True)
    embed_update.add_field(name = 'Percent Change', value = googlePercent, inline = True)
    embed_update.add_field(name = '====================================', value = '====================================', inline = False)
    embed_update.add_field(name = 'Amazon', value = '-------------------', inline = False)
    embed_update.add_field(name = 'Current Price', value = amazonPrice, inline = True)
    embed_update.add_field(name = 'Current Shares', value = amazonShares, inline = True)
    embed_update.add_field(name = 'Percent Change', value = amazonPercent, inline = True)
    embed_update.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed_update)
    insertRow = [googlePrice, amazonPrice]
    stock_logs.append_row(insertRow)

@client.command()
async def market2(ctx):
    embed_update2 = discord.Embed(
        title = 'Live Stock Viewer',
        description = 'All available stocks can be viewed here in real time.'
    )
    cocaPrice = stock_list.acell('B10').value
    cocaShares = stock_list.acell('D10').value
    cocaPercent = stock_list.acell('C10').value

    pepsiPrice = stock_list.acell('B12').value
    pepsiShares = stock_list.acell('D12').value
    pepsiPercent = stock_list.acell('C12').value

    timesPrice = stock_list.acell('B13').value
    timesShares = stock_list.acell('D13').value
    timesPercent = stock_list.acell('C13').value

    petrolePrice = stock_list.acell('B14').value
    petroleShares = stock_list.acell('D14').value
    petrolePercent = stock_list.acell('C14').value

    motorPrice = stock_list.acell('B16').value
    motorShares = stock_list.acell('D16').value
    motorPercent = stock_list.acell('C16').value

    embed_update2.add_field(name = 'Coca Cola CO', value = '-------------------', inline = False)
    embed_update2.add_field(name = 'Current Price', value = cocaPrice, inline = True)
    embed_update2.add_field(name = 'Current Shares', value = cocaShares, inline = True)
    embed_update2.add_field(name = 'Percent Change', value = cocaPercent, inline = True)
    embed_update2.add_field(name = '====================================', value = '====================================', inline = False)
    embed_update2.add_field(name = 'Pepsi Co', value = '-------------------', inline = False)
    embed_update2.add_field(name = 'Current Price', value = pepsiPrice, inline = True)
    embed_update2.add_field(name = 'Current Shares', value = pepsiShares, inline = True)
    embed_update2.add_field(name = 'Percent Change', value = pepsiPercent, inline = True)
    embed_update2.add_field(name = '====================================', value = '====================================', inline = False)
    embed_update2.add_field(name = 'New York Times', value = '-------------------', inline = False)
    embed_update2.add_field(name = 'Current Price', value = timesPrice, inline = True)
    embed_update2.add_field(name = 'Current Shares', value = timesShares, inline = True)
    embed_update2.add_field(name = 'Percent Change', value = timesPercent, inline = True)
    embed_update2.add_field(name = '====================================', value = '====================================', inline = False)
    embed_update2.add_field(name = 'Marathon Petrole', value = '-------------------', inline = False)
    embed_update2.add_field(name = 'Current Price', value = petrolePrice, inline = True)
    embed_update2.add_field(name = 'Current Shares', value = petroleShares, inline = True)
    embed_update2.add_field(name = 'Percent Change', value = motorPercent, inline = True)
    embed_update2.add_field(name = '====================================', value = '====================================', inline = False)
    embed_update2.add_field(name = 'General Motors', value = '-------------------', inline = False)
    embed_update2.add_field(name = 'Current Price', value = motorPrice, inline = True)
    embed_update2.add_field(name = 'Current Shares', value = motorShares, inline = True)
    embed_update2.add_field(name = 'Percent Change', value = motorPercent, inline = True)
    embed_update2.add_field(name = '====================================', value = '====================================', inline = False)
    await ctx.send(embed=embed_update2)
    insertRow = [cocaPrice, pepsiPrice]
    stock_logs.append_row(insertRow)


@client.command()
async def view(ctx):

    findID = ctx.author.id
    foundID = stock_data.findall(str(findID))
    if foundID == None:
        embed_denied = discord.Embed(
            title = 'TERMINAL ACCESS DENIED',
            description = 'USER NOT FOUND'
        )
        await ctx.send(embed=embed_denied)
    else:
        print(week)
        if week == 5 or week == 6:
            embed_notice = discord.Embed(
                title = 'New York Stock Market',
                description = 'The NYSM is open from Monday to Friday, 9:30am to 4:00pm EST'
            )
            embed_notice.add_field(name = 'Status', value = 'Closed')
            await ctx.send(embed=embed_notice)
        else:
            if hour > openHour and hour < closeHour:
                embed_notice = discord.Embed(
                    title = 'New York Stock Market',
                )
                embed_notice.add_field(name='Status', value = 'Open')
                await ctx.send(embed=embed_notice)
            if hour < openHour or hour > closeHour:
                embed_notice = discord.Embed(
                    title = 'New York Stock Market',
                    description = 'The NYSM is open from Monday to Friday, 9:30am to 4:00pm EST'
                )
                embed_notice.add_field(name='Status', value = 'Closed')
                await ctx.send(embed=embed_notice)
        if len(foundID)<=4:
            amountofpurchases = len(foundID)

            embed_view = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )

            for i in range(len(foundID)):
                row = (foundID[i]).row
                dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                embed_view.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                embed_view.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                embed_view.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                embed_view.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                embed_view.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                embed_view.add_field(name= 'Profit', value=dataView[5][0][0])
            await ctx.send(embed = embed_view)
        if len(foundID)>4:

            amountofpurchases = len(foundID)

            embed_view = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )

            for i in range(4):
                row = (foundID[i]).row
                print(row)
                dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                embed_view.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                embed_view.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                embed_view.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                embed_view.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                embed_view.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                embed_view.add_field(name= 'Profit', value=dataView[5][0][0])
            await ctx.send(embed = embed_view)
            embed_view2 = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )
            print(foundID)
            print(f"len found id = {len(foundID)}")
            for i in range(len(foundID)-4):
                    row = (foundID[i+4]).row

                    print(row)
                    print(f"i = {i}")
                    dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                    embed_view2.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                    embed_view2.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                    embed_view2.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                    embed_view2.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                    embed_view2.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                    embed_view2.add_field(name= 'Profit', value=dataView[5][0][0])
                    print('worked')
            await ctx.send(embed = embed_view2)

@client.command()
@commands.has_role('Stock Broker')
async def adminview(ctx,findID):

    foundID = stock_data.findall(str(findID))
    if foundID == None:
        embed_denied = discord.Embed(
            title = 'TERMINAL ACCESS DENIED',
            description = 'USER NOT FOUND'
        )
        await ctx.send(embed=embed_denied)
    else:
        if len(foundID)<=4:
            amountofpurchases = len(foundID)

            embed_view = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )

            for i in range(len(foundID)):
                row = (foundID[i]).row
                dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                embed_view.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                embed_view.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                embed_view.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                embed_view.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                embed_view.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                embed_view.add_field(name= 'Profit', value=dataView[5][0][0])
            await ctx.send(embed = embed_view)
        if len(foundID)>4:

            amountofpurchases = len(foundID)

            embed_view = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )

            for i in range(4):
                row = (foundID[i]).row
                print(row)
                dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                embed_view.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                embed_view.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                embed_view.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                embed_view.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                embed_view.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                embed_view.add_field(name= 'Profit', value=dataView[5][0][0])
            await ctx.send(embed = embed_view)
            embed_view2 = discord.Embed(
                title = 'TERMINAL ACCESS GRANTED',
                description = f"USER = {findID}  ║  Date = {today}"
            )
            print(foundID)
            print(f"len found id = {len(foundID)}")
            for i in range(len(foundID)-4):
                    row = (foundID[i+4]).row

                    print(row)
                    print(f"i = {i}")
                    dataView = stock_data.batch_get([f'A{row}',f'B{row}',f'D{row}',f'E{row}',f'I{row}',f'J{row}',f'K{row}',f'F{row}'])
                    embed_view2.add_field(name= f"ID: {dataView[0][0][0]} ║ TICKER = {dataView[2][0][0]}", value = '------------------------------------', inline = False)
                    embed_view2.add_field(name= 'Original Value', value = dataView[3][0][0], inline = True)
                    embed_view2.add_field(name = 'Current Value', value = dataView[4][0][0], inline = True)
                    embed_view2.add_field(name = 'Shares', value = dataView[7][0][0], inline = True)
                    embed_view2.add_field(name= 'Percent Change', value = dataView[6][0][0], inline = True)
                    embed_view2.add_field(name= 'Profit', value=dataView[5][0][0])
                    print('worked')
            await ctx.send(embed = embed_view2)

# def next_availble_row(stock_logs):
#     str_list = list(filter(None, stock_logs.col_values(1)))
#     return str(len(str_list)+1)

@client.command()
@commands.has_role('Stock Broker')
async def sell(ctx, buyer: discord.User = None, ticker = None, shares = None):
    author = ctx.message.author

    buyer = buyer.id
    if ticker == None and buyer == None and shares == None:
        await respond(ctx, 'You are missing arguments: .sell <ticker> <amount of shares>')
    if ticker != None and shares == None:
        await respond(ctx, 'You are missing arguments: .sell <ticker> <amount of shares>')
    if ticker != None and shares != None:
        available_ticker = ['AAPL','STAA','F','IBM','MRO','KO','PEP','NYT','MPC','GM','VZ','CPU','HRB','SHLDQ','BKNG','BRK.A','NVR','GOOG','SEB','NXT', 'LISN']
        if ticker not in available_ticker:
            await respond(ctx, 'You have provided an invalid ticker:')
            await respond(ctx, available_ticker)
        else:
            await registerCheck(ctx)
            buyerInfo = stock_name.find(str(buyer))
            findTicker = stock_list.find(ticker)
            priceTickerRow = (findTicker).row
            priceTicker = stock_list.cell(priceTickerRow, 2).value
            priceTickerForm = priceTicker.replace('$','')
            priceTickerForm2 = priceTickerForm.replace(',','')
            pay = float(priceTickerForm2) * float(shares)
            randPurchaseID =  random.randint(1111,9999)
            perShare = float(pay) / float(shares)
            curValue = f"=GOOGLEFINANCE(\"{ticker}\")*{shares}"
            difValue = f"=GOOGLEFINANCE(\"{ticker}\")*{shares}-{pay}"
            percent = f"=GOOGLEFINANCE(\"{ticker}\")*{shares}/{pay}-1"

            buyerInfoRow = buyerInfo.row
            buyerInfoFName = stock_name.cell(buyerInfoRow,2).value
            buyerInfoLName = stock_name.cell(buyerInfoRow,3).value

            company = stock_list.cell(priceTickerRow,8).value

            insertRow = [str(randPurchaseID),str(author), str(buyer), str(ticker), str(pay), str(shares),f"=GOOGLEFINANCE(\"{ticker}\")", perShare, curValue,difValue,percent,str(today),buyerInfoFName,buyerInfoLName,str(company)]
            stock_data.append_row(insertRow, value_input_option='USER_ENTERED')



            embed = discord.Embed(
                title = 'Purchase Receipt',
                description = 'All relevant information of your purchase will be present here.'
            )
            embed.add_field(name='Client Information', value = str(buyer))
            embed.add_field(name='Purchase Id', value = randPurchaseID)
            embed.add_field(name='Ticker', value = ticker)
            embed.add_field(name='Shares', value = shares)
            embed.add_field(name='Transaction', value = f"{pay}$")
            embed.add_field(name='Purchase Value', value = priceTicker)
            embed.set_footer(text='Contact an accountant for any inquiries.')
            await ctx.send(embed=embed)

@client.command()
# @commands.has_role('ROLE') SET ROLE
async def sale(ctx, ID = None):
    if ID == None:
        await respond(ctx, 'To view a receipt: .sale <Purchase ID>')
    else:
        findID = stock_data.find(str(ID))
        if findID == None:
            embed_denied = discord.Embed(
                title = 'Receipt Access Denied',
                description = 'RECEIPT ID NOT FOUND'
            )
            await ctx.send(embed=embed_denied)
        else:
            embed_id = discord.Embed(
                title = 'Receipt Access Granted',
                description = 'All information found will be shown here.'
            )
            findIDRow = findID.row
            names = ['Purchase ID', 'Contractor', 'Client ID', 'Ticker', 'Transaction', 'Shares Bought', 'Purchase Value']
            for i in range(6):
                data = stock_data.cell(findIDRow, i+1).value
                embed_id.add_field(name = names[i], value=str(data))
            receipt = stock_data.cell(findIDRow, 16).value
            embed_id.add_field(name='Receipt', value=receipt)

            await ctx.send(embed=embed_id)

@client.command()
async def value(ctx, ticker = None, price = None):
    if ticker == None and price == None:
        await respond(ctx, '.value <ticker> <planned investement (ex: 50000)>')
    if ticker != None and price == None:
        await respond(ctx, '.value <ticker> <planned investement (ex: 50000)>')
    if ticker != None and price != None:
        tickerFind = stock_list.find(str(ticker))
        tickerRow = tickerFind.row
        tickerPrice = stock_list.cell(tickerRow, 2).value
        priceTickerForm = tickerPrice.replace('$','')
        priceTickerForm2 =priceTickerForm.replace(',','')
        invest = float(price)/ float(priceTickerForm2)
        embed = discord.Embed(
            title = 'Stock Market Calculator'
        )
        embed.add_field(name='Ticker',value=ticker,inline=False)
        embed.add_field(name='Amount Invested',value=f"{price}$",inline=True)
        embed.add_field(name='Shares',value=invest,inline=True)
        await ctx.send(embed=embed)

@client.command()
async def commandsk(ctx):
    embed = discord.Embed(
        title = 'COMMANDS INFO',
        description = 'Here you can find all the availble commands and their usage. To view the command parameters just type the command.'
    )
    embed.add_field(name='.view', value='View available shares that you own and their informations.')
    embed.add_field(name='.sale', value='View a receipt after a purchase.')
    embed.add_field(name='.value', value='Find the amount of shares for a specific investment amount.')
    embed.add_field(name='.stock', value='View a sotcks data.')
    embed.add_field(name='.register', value='Register into the New York Stock Exchange.')
    await ctx.send(embed=embed)

@client.command()
async def stock(ctx, ticker):
    tickerRow = stock_list.find(ticker).row
    data = stock_list.row_values(tickerRow)
    embed = discord.Embed(
        title = 'Stock Data Viewer',
        description = 'All relevant information on a stock will be shown here.'
    )
    embed.add_field(name='Ticker', value=ticker, inline=True)
    embed.add_field(name='Name',value=data[7],inline = True)
    embed.add_field(name = '====================================', value = '====================================', inline = False)
    embed.add_field(name='Current Value', value=data[1],inline = True)
    embed.add_field(name='Percent Change', value = data[2],inline = True)
    embed.add_field(name = '====================================', value = '====================================', inline = False)
    embed.add_field(name='Total Shares', value = data[3], inline = True)
    embed.add_field(name='Highest Price', value = data[4], inline = True)
    embed.add_field(name='Lowest Price', value = data[5],inline = True)
    await ctx.send(embed=embed)

@client.command()
async def tos(ctx):
    embed = discord.Embed(
        title = 'TERMINAL TOS'
    )
    embed.add_field(name='Investment Cap',value='All Investments are capped at 200,000$ per stock. For higher investments, approval would be necessary.')
    embed.add_field(name='Sale Limit', value='Shares can only be sold 1 week after purchse.')
    embed.add_field(name='Share Trade', value='Shares may be transfered or traded.')
    await ctx.send(embed=embed)

@client.command()
async def register(ctx, first = None, last = None):

    if first == None and last == None:
        await respond(ctx, 'To Register: .register <First Name> <Last Name>')
    if first != None and last == None:
        await respond(ctx, 'To Register: .register <First Name> <Last Name>')
    if first != None and last != None:
        author = ctx.message.author.id
        findAuthor = stock_name.find(str(author))
        if findAuthor != None:
            findAuthorRow = findAuthor.row
            findAuthorFirst = stock_name.cell(findAuthorRow,2).value
            findAuthorLast = stock_name.cell(findAuthorRow,3).value
            findAuthroDate = stock_name.cell(findAuthorRow,4).value
            embed = discord.Embed(
                title = 'REGISTRATION FAILED',
                description = 'If you believe this is a mistake, contact a stock broker.'
            )
            embed.add_field(name='ERROR TYPE',value='Client is already registered', inline = False)
            embed.add_field(name='First Name',value=findAuthorFirst,inline = True)
            embed.add_field(name='Last Name',value=findAuthorLast,inline = True)
            embed.add_field(name='Registration Date', value=findAuthroDate,inline = False)
            await ctx.send(embed=embed)
        if findAuthor == None:
            embed = discord.Embed(
                title = 'REGISTRATION SUCESSFUL',
                description = 'Your registration has been logged in the New York Stock Exchange database.'
            )
            embed.add_field(name='First Name', value=first)
            embed.add_field(name='Last Name', value=last)
            embed.add_field(name='Registration Terms', value='By registrating, you confirm that the provided data is valid.',inline=False)
            await ctx.send(embed=embed)
            insertRow = [str(author), str(first), str(last), str(today)]
            stock_name.append_row(insertRow)

@client.command()
async def template(ctx):
    embed = discord.Embed(
        title = 'Receipt Template'
    )
    embed.add_field(name='Link',value='https://docs.google.com/document/d/1a7RQXuTU8uOtHvfWpO9Iw-A9GSvn5Y8lL66KprjGM5g/edit?usp=sharing')
    await ctx.send(embed=embed)
@client.command()
async def stocks(ctx):
    await ctx.send('https://imgur.com/a/ekw0jE2')

@client.command()
async def portfolio(ctx):
    await registerCheck(ctx)
    user = ctx.message.author.id
    userFindRow = stock_name.find(str(user)).row
    dataGet = stock_name.row_values(userFindRow)
    if dataGet[4] == 'https://i.imgur.com/SQgZvnM.png':
        embed = discord.Embed(
        title = f"Mr. {dataGet[2]}\'s Portfolio",
        description = 'You do not have a profile picture. .pfp <url>'
        )
    else:
        embed = discord.Embed(
            title = f"Mr. {dataGet[2]}\'s Portfolio",
            # description = f"dataGet[10]"
        )
    embed.set_thumbnail(url=dataGet[4])
    embed.add_field(name = 'Total Profit', value = dataGet[5])
    embed.add_field(name = 'Total Purchases', value = dataGet[6])
    embed.add_field(name = 'Total Invested', value = dataGet[7])
    embed.add_field(name = 'Total Investments Value', value = dataGet[8])
    await ctx.send(embed=embed)

@client.command()
async def pfp(ctx, url):
    await registerCheck(ctx)
    user = ctx.message.author.id
    findUser = stock_name.find(str(user)).row
    store = stock_name.update_cell(findUser, 5, url)
    await ctx.send(f"Your profile picture has been changed.")

@client.command()
@commands.has_role('Stock Broker')
async def adminprofile(ctx, user):
    userFind = stock_name.find(str(user))
    if userFind == None:
        await respond(ctx, 'This User is not registered')
    else:
        userFindRow = userFind.row
        dataGet = stock_name.row_values(userFindRow)
        if dataGet[4] == 'https://i.imgur.com/SQgZvnM.png':
            embed = discord.Embed(
            title = f"Mr. {dataGet[2]}\'s Portfolio",
            description = 'You do not have a profile picture. .pfp <url>'
            )
        else:
            embed = discord.Embed(
                title = f"Mr. {dataGet[2]}\'s Portfolio"
            )
        embed.set_thumbnail(url=dataGet[4])
        embed.add_field(name = 'Total Profit', value = dataGet[5])
        embed.add_field(name = 'Total Purchases', value = dataGet[6])
        embed.add_field(name = 'Total Invested', value = dataGet[7])
        embed.add_field(name = 'Total Investments Value', value = dataGet[8])
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Stock Broker')
async def invest(ctx, amount):
    embed = discord.Embed(
        title = 'New York Stock Market Value',
        description = f"Currently ${amount} was invested in the NYSM."
    )
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('Stock Broker')
async def inv(ctx, amount):
    channel = client.get_channel(935250746209865759)
    msg = await channel.fetch_message(929178778201112636)
    await asyncio.sleep(1)
    embed2 = discord.Embed(
        title = 'New York Stock Market Value',
        description = f"Currently ${amount} was invested in the NYSM."
    )
    await msg.edit(embed = embed2)

@client.command()
@commands.has_role('Stock Broker')
async def clear(ctx, ticketID):
    caller = ctx.author.id
    broker = ctx.author
    findSale = stock_data.find(ticketID)
    findSaleRow = findSale.row
    stock_data.update(f"C{findSaleRow}:K{findSaleRow}", [['SOLD','SOLD','SOLD','SOLD','SOLD','SOLD','SOLD','SOLD','SOLD']])
    stock_data.format(f"C{findSaleRow}:K{findSaleRow}",{
        "backgroundColor": {
        "red": 56.0,
        "green": 56.0,
        "blue": 56.0
        },
        "horizontalAlignment": "CENTER",
        "textFormat": {
        "foregroundColor": {
            "red": 200.0,
            "green": 200.0,
            "blue": 200.0
        },
        "fontSize": 10,
        "bold": True
        }
    })
    # insertRow = [str(today), str(broker)]
    # stock_sale.append_row(insertRow)
    await respond(ctx, f"Sale #{ticketID} has been marked as sold")

@client.command()
@commands.dm_only()
async def bank(ctx, bankNumber = None):
    caller = ctx.author.id
    callerFind = stock_name.find(str(caller))
    if callerFind == None:
        embed_denied = discord.Embed(
            title = 'TERMINAL ACCESS DENIED',
            description = 'USER NOT FOUND <.register>'
        )
        await ctx.send(embed=embed_denied)
    if callerFind != None:
        if bankNumber == None:
            await respond(ctx, '.bank <bank #>')
        if bankNumber != None:
            callerRow = callerFind.row
            stock_name.update(f"J{callerRow}", bankNumber)
            embed = discord.Embed(
                title = 'Information Successfully Saved',
                description = f"BANK#: {bankNumber}"
            )
            await ctx.send(embed=embed)

@client.command()
async def refer(ctx, referred: discord.Member = None):
    caller = ctx.author
    callerDupe = stock_refe.find(str(caller))
    if callerDupe == None:
        embed = discord.Embed(
            title = 'Referral',
            description = 'Thank you for referring a stock broker'
        )
        embed.add_field(name = 'Stock Broker', value = f"{referred}")
        referredID = referred.id
        insertRow = [str(caller), str(referredID)]
        stock_refe.append_row(insertRow)
        await ctx.send(embed = embed)
    if callerDupe != None:
        await respond(ctx, 'You have already referred a stock broker.')

@client.command()
@commands.has_role('Stock Broker')
async def refer_check(ctx):
    caller = ctx.author.id
    callerSearch = stock_refe.findall(str(caller))
    embed = discord.Embed(
        title = 'Referral check',
        description = f"{len(callerSearch)}"
    )
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('Stock Broker')
async def refer_pay(ctx, broker: discord.Member = None, pay = None):
    if broker == None:
        await respond(ctx, '.refer_pay <stock broker mention> pay')
    if broker != None and pay == None:
        embed = discord.Embed(
            title = 'Referral Payment',
            description = 'This will tell you how many  referrals a stock broker has.'
        )
        brokerReferrals = stock_refe.findall(str(broker.id))
        embed.add_field(name = broker, value = len(brokerReferrals))
        await ctx.send(embed=embed)
    if broker != None and pay == 'pay':
        payout = 2500
        embed = discord.Embed(
            title = 'Referral Payement',
            description = 'Stock Brokers recieve 2,500$/referrals'
        )
        brokerReferrals = stock_refe.findall(str(broker.id))

        embed.add_field(name = f"{broker} Total Payout", value = (len(brokerReferrals)*2500))
        for i in range(len(brokerReferrals)):
            brokerReferralsRow = brokerReferrals[i].row
            stock_refe.update(f"B{brokerReferralsRow}",[['PAYED']])
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Director') # add role
async def broker(ctx, name = None):

    if name == None:
        await respond(ctx, '.broker <name>')
    if name != None:
        output = stock_brok.find(str(name))
        if output == None:
            await respond(ctx, f"No results found for {name}")
        if output != none:
            embed = discord.Embed(
                title = 'Broker',
                description = 'Output from your search'
            )
            embed.add_field(name = x, value = x) # first name last name
            embed.add_field(name = y, value = y) # discord tag
            embed.add_field(name = z, value = z) # employee ID
            embed.add_field(name = 'Date Hired', value = w) # date hired
            await ctx.send(embed = embed)

client.run('OTQ2MDU0NzcwMjU3NDQ5MDIw.YhZIKg.C8mubhxolGO1P0cKUikdoZxoysE')
