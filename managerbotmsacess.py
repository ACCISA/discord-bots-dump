import discord
import random
import aiofiles
import os.path
from asyncio import sleep
import sqlite3
from dotenv import load_dotenv
# import discord-components
import discord_components
# from discord_buttons import *
from discord_components import *
from discord_components.client import DiscordComponents
import pandas as pd
from random import randint
from discord.ext import commands, tasks
import pyodbc

load_dotenv()
client = commands.Bot(command_prefix = '.', help_command=None)
client.remove_command('help')
clients = discord.Client(activity=discord.Game(name='my game'))
activity = discord.Activity(name='The Empire Grow', type=discord.ActivityType.watching)
clients = discord.Client(activity=activity)

#logs guns
if not (os.path.isfile('logs.csv')):
    data = pd.DataFrame(columns=['USER','GUN(S)','PRICE']) #Constructing dataframe.
    data.to_csv("logs.csv",index=False)

#logs product
if not (os.path.isfile('Prod.csv')):
    data1 = pd.DataFrame(columns=['USER','AMOUNT','PRICE']) #Constructing dataframe.
    data1.to_csv("Prod.csv",index=False)

#logs recruits
if not (os.path.isfile('Recruit.csv')):
    data2 = pd.DataFrame(columns=['USER','RECRUIT','AMOUNT']) #Constructing dataframe.
    data2.to_csv("Recruit.csv",index=False)

#logs member strikes
if not (os.path.isfile('Strikes.csv')):
    data3 = pd.DataFrame(columns=['USER','MEMBER','REASON']) #Constructing dataframe.
    data3.to_csv("Strikes.csv",index=False)


client.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}


#Debugging status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name="The Empire Grow"
    ))

    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    db.commit()
    print('Bot is online.')
    DiscordComponents(client)

#files button command
# @client.command()
# async def button(ctx):
#     n = await ctx.send(
#         "Button Command Ran!",
#         buttons=[
#             Button(style=ButtonStyle.blue, label="Click me!"),
#             Button(style=ButtonStyle.URL, label="File", url="https://youtube.com"),

#         ],
#     )
#     res = await ddb.wait_for_button_click(n)
#     await res.respond(
#         type=InteractionType.ChannelMessageWithSource,
#         content=f'{res.button.label} has been clicked'
#     )


#dm command
@client.command()
async def dm(ctx, member:discord.Member, *, args=None):
    embed = discord.Embed(
        title = 'Mail Box',
        description = 'You find a letter in your mail box indicating a new task. You do not know who sent it or where it came from, but you do not question it.',
        colour  = discord.Colour.red()
    )
    embed.add_field(name='New Letter', value=args)
    embed.set_footer(text='OOC= Romullus#0001 for any questions, FYI this is IC')
    embed.set_thumbnail(url='https://i.imgur.com/tJLWIEx.png')
    embed.set_image(url='https://i.imgur.com/ThZhph9.png')

    if member != None and args != None:
      await member.send(embed=embed)

      await ctx.channel.send("The message has been sent")

    else:
        await ctx.channel.send("This person does not exist or is not in the server")
#dm command end


@client.command()
async def files(ctx):
    embed = discord.Embed(
        title = 'Files and Documentation',
        description = 'Here  you will find all the info you will need.',
        colour = discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://i.imgur.com/WOUMnA1.png')

    await ctx.send(
        embed=embed,
        components = [
            Button(style=ButtonStyle.URL, label='La Ruana Pistols Prices', url="https://docs.google.com/document/d/1jkCMvomyOHj29wlH7je86wKU24jBn3bDKYJ8n6e7MNk/edit?usp=sharing"),
            Button(style=ButtonStyle.URL, label='La Ruana Pistols Sales', url="https://docs.google.com/spreadsheets/d/1inNwrOy5vqU6uIoMC56RY__VtJObmr34fewCTO5bfT8/edit?usp=sharing"),
            Button(style=ButtonStyle.URL, label='Firearm License Application', url="https://discord.gg/zWAHbd9axq"),
            Button(style=ButtonStyle.URL, label='Bar Certification Exam', url="https://discord.gg/CekBEzAeSj"),
            Button(style=ButtonStyle.URL, label='NPC Locations + Map', url="https://cdn.discordapp.com/attachments/820410175684083722/857463475009749002/image0.png"),
            Button(style=ButtonStyle.URL, label='Diverge Rules', url='https://divergenet.works/forums/forumdisplay.php?fid=34')
        ],

    )
    #interaction once button is clicked
    # interaction2 = await client.wait_for("button_click", check=lambda i: i.component.label.startswith("Firearm"))
    # await interaction2.repsond(content="Go into #appliying-for-license")

#motel info
@client.command()
async def motel(ctx):
    embed = discord.Embed(
        title = 'Motel California',
        description = 'Here  you will find all the info you will need.',
        colour = discord.Colour.blue()
    )
    embed.add_field(name='Permission', value='Before selling any room at the motel, you must make sure that you have the permission to sell rooms.')
    embed.add_field(name='Process', value='To sell a room, firsly you must ask for their ID to verify that they are who they claim to be')
    embed.set_thumbnail(url='https://i.imgur.com/WOUMnA1.png')

    await ctx.send(
        embed=embed,
        components = [
            Button(style=ButtonStyle.URL, label='La Ruana Pistols Prices', url=""),
            Button(style=ButtonStyle.URL, label='La Ruana Pistols Sales', url=""),
            Button(style=ButtonStyle.URL, label='Firearm License Application', url=""),
            Button(style=ButtonStyle.URL, label='Bar Certification Exam', url=""),
            Button(style=ButtonStyle.URL, label='NPC Locations + Map', url=""),
        ],

    )
    #interaction once button is clicked
    # interaction2 = await client.wait_for("button_click", check=lambda i: i.component.label.startswith("Firearm"))
    # await interaction2.repsond(content="Go into #appliying-for-license")


#help system
@client.command(pass_context = True) #to get USERv
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.red()

    )

    embed.set_author(name='Help')
    embed.add_field(name='gun', value='Use this command to log an illegal gun sale.', inline = False)
    embed.add_field(name='clear', value='Clears chat, add a number at the end for specificity.', inline = False)
    embed.add_field(name='freq', value='Randomises a frequency each day for security reasons.', inline = False)
    embed.add_field(name='warn', value='Gives a cartel member a strike.', inline = False)
    embed.add_field(name='warnings', value='Verifies strikes issued to a cartel member', inline = False)




    await author.send(embed=embed)


#cartel strike system start
@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}

#logs Guns
@client.command()
async def gun(ctx,Gun,Sale):

    data_Dict={'USER' : str(ctx.author),
                'GUN(S)' : str(Gun),
                'PRICE':str(Sale)}
    try:
        data = pd.read_csv('logs.csv')
        data = data.append({'USER': data_Dict['USER'],
                            'GUN(S)':data_Dict['GUN(S)'],
                            'PRICE':data_Dict['PRICE']},ignore_index=True)
        #Save the data to .csv
        data.to_csv("logs.csv",index=False) #Saving the dataframe
        await ctx.send(f"**Succesfully saved**\n**Gun** = {str(Gun)}\n**Price** = {str(Sale)}")
    except Exception as e:
        print(e)
#end Guns logs

#Prod Logs
@client.command()
async def prod(ctx,Amount,Price):

    data_Dict={'USER' : str(ctx.author),
                'AMOUNT' : str(Amount),
                'PRICE':str(Price)}
    try:
        data = pd.read_csv('Prod.csv')
        data = data.append({'USER': data_Dict['USER'],
                            'AMOUNT':data_Dict['AMOUNT'],
                            'PRICE':data_Dict['PRICE']},ignore_index=True)
        #Save the data to .csv
        data.to_csv("Prod.csv",index=False) #Saving the dataframe
        await ctx.send(f"**Succesfully saved**\n**Amount** = {str(Amount)}\n**Price** = {str(Price)}")
    except Exception as e:
        print(e)
#end Prod logs

# start recruit logs
@client.command()
async def recruit(ctx,Recruit,Price):

    data_Dict2={'USER' : str(ctx.author),
                'RECRUIT' : str(Recruit),
                'PRICE':str(Price)}
    try:
        data2 = pd.read_csv('Recruit.csv')
        data2 = data2.append({'USER': data_Dict2['USER'],
                            'RECRUIT':data_Dict2['RECRUIT'],
                            'PRICE':data_Dict2['PRICE']},ignore_index=True)
        #Save the data to .csv
        data2.to_csv("Recruit.csv",index=False) #Saving the dataframe
        await ctx.send(f"**Succesfully saved**\n**Recruit's Name** = {str(Recruit)}\n**Amount Spent** = {str(Price)}")
    except Exception as e:
        print(e)
# #end recruit logs

#start member strikes logs
def is_it_me_strike(ctx):
    return ctx.author.id == 248200896738099200, 270608372334592000, 252187604764721163, 269926950276038657, 223098452253343744, 641491004893167618, 534877525260894210

@client.command()
@commands.check(is_it_me_strike)
async def strike(ctx,Member,Reason):

    data_Dict3={'USER' : str(ctx.author),
                'MEMBER' : str(Member),
                'REASON':str(Reason)}
    try:
        data3 = pd.read_csv('Strikes.csv')
        data3 = data3.append({'USER': data_Dict3['USER'],
                            'MEMBER':data_Dict3['MEMBER'],
                            'REASON':data_Dict3['REASON']},ignore_index=True)
        #Save the data to .csv
        data3.to_csv("Strikes.csv",index=False) #Saving the dataframe
        await ctx.send(f"**Succesfully saved**\n**Members's Name** = {str(Member)}\n**Reason** = {str(Reason)}")
    except Exception as e:
        print(e)
#end of member strikes logs

@client.command()
@commands.has_permissions(administrator = True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("This person is not part of the cartel or you have misspelled his name.")

    if reason is None:
        return await ctx.send("You must provide a reason for this strike.")

    try:
        first_strike = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_strike = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
            await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'strikes' if first_strike else 'strikes'}.")

@client.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("This person is not part of the cartel or you have misspelled his name.")

    embed = discord.Embed(title=f"Display strikes for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Strike {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: #no warnings
        await ctx.send("This cartel member has no strikes.")
#end of striking system

#command to clear chat with specific int
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#use this to do a command for specific people add or and the copy id
#248200896738099200 = Romullus
#376869273668288542 = scoota
#freq start
def is_it_me_freq(ctx):
    return ctx.author.id == 248200896738099200

@client.command()
@commands.check(is_it_me_freq)
async def freq(ctx, enabled="start", interval=86400,):
    if enabled.lower() == "stop":
        messageInterval.stop()
    elif enabled.lower() == "start":
        messageInterval.change_interval(seconds=int(interval))
        messageInterval.start(ctx, random.randint(100,899))

@tasks.loop(seconds=86400)
async def messageInterval(ctx, message):
    await ctx.send(f'Frequency Changed to **{random.randint(100,899)}**')

#beginning calculator testing
@client.event
async def on_ready():
	print('Ready.')

def add(n: float, n2: float):
	return n + n2

def sub(n: float, n2: float):
	return n - n2

def rando(n: int, n2: int):
	return random.randint(n, n2)

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2

@client.command()
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathrando(ctx, x: int, y: int):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def profithc(ctx, x: float, y: float):
    result = abs((y*8600)-(x*2000))
    result2 = abs((x*6000)-(y*4000))
    fair = abs(((result)-(result2))/2)
    embed = discord.Embed(
    colour = discord.Colour.red()

    )

    embed.set_author(name='Profit Calculator for Coke')
    embed.add_field(name='H Profit', value=result, inline = True)
    embed.add_field(name='C Profit', value=result2, inline = True)
    embed.add_field(name='Fair Trade Tax', value=fair, inline = False)
    await ctx.send(embed=embed)

@client.command()
async def profithw(ctx, x: float, y: float):
    result = abs((y*6800)-(x*2000))
    result2 = abs((x*6000)-(y*2500))
    fair = abs(((result)-(result2))/2)
    embed = discord.Embed(
    colour = discord.Colour.red()

    )

    embed.set_author(name='Profit Calculator for Weed')
    embed.add_field(name='H Profit', value=result, inline = True)
    embed.add_field(name='W Profit', value=result2, inline = True)
    embed.add_field(name='Fair Trade Tax', value=fair, inline = False)
    await ctx.send(embed=embed)

@client.command()
async def profithmq(ctx, x: float, y: float):
    result = abs((y*5600)-(x*2000))
    result2 = abs((x*6000)-(y*2000))
    fair = abs(((result)-(result2))/2)
    embed = discord.Embed(
    colour = discord.Colour.red()

    )

    embed.set_author(name='Profit Calculator for MQ')
    embed.add_field(name='H Profit', value=result, inline = True)
    embed.add_field(name='W Profit', value=result2, inline = True)
    embed.add_field(name='Fair Trade Tax', value=fair, inline = False)
    await ctx.send(embed=embed)


@client.command()
async def profitho(ctx, x: float, y: float):
    result = ((y*5000)-(x*2000))
    if result < 0:
        ctx.send("You are losing money")

    else:
        embed = discord.Embed(
        colour = discord.Colour.red()

        )

        embed.set_author(name='Profit Calculator for Opium')
        embed.add_field(name='Your Profit', value=result, inline = False)
        await ctx.send(embed=embed)

@client.command()
async def profithm(ctx, x: float, y: float):
    result = ((y*5600)-(x*2000))

    ctx.send("You are losing money")


    embed = discord.Embed(
    colour = discord.Colour.red()

    )

    embed.set_author(name='Profit Calculator for Opium')
    embed.add_field(name='Your Profit', value=result, inline = False)
    await ctx.send(embed=embed)

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\darra\OneDrive\Documents\python.accdb;'
    conn =  pyodbc.connect(con_string)
    print("Connected to Database")


except pyodbc.Error as e:
    print("Error in connection", e)


@client.command()
async def test(ctx,name,gmail):
    if len(name) == 0:
        await ctx.send("**Error**: Please provide your name/discord + the amount of h to sell")

    else:
    # id = last()
        cursor= conn.cursor()
        cursor.execute("INSERT INTO users(Name, Email) VALUES (?, ?)", (name, gmail))
        conn.commit()
        await ctx.send("Database Updated")

@client.command()
async def view(ctx):
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM users")

    for x in cursor:
        embed = discord.Embed(
        colour = discord.Colour.red()

        )

        embed.add_field(name=x)
        await ctx.send(embed=embed)

@client.command()
async def users(ctx):
    cursor= conn.cursor()
    cursor.execute("SELECT Username, Author FROM inventory")

    for x in cursor:
        await ctx.send(x)


@client.command()
async def marketregister(ctx,name):

    author = str(ctx.author) # to get USER
    cursor= conn.cursor()
    cursor.execute("INSERT INTO inventory(Username, Author) VALUES (?, ?)", (name, author))
    conn.commit()
    await ctx.send(f'**{name}** has been registered into to the database.')

@client.command()
async def marketadd(ctx,amount,price):

    author = str(ctx.author) # to get USER
    cursor= conn.cursor()
    cursor.execute("UPDATE inventory SET Amount = ?, Price = ? WHERE Author = ? ", (amount, price, author))
    conn.commit()
    await ctx.send(f'You are selling **{amount}** for {price}$ each.')

client.run('')
