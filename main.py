import json, time, discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime
from colorama import Fore, init

init()

class Status:
    roles = 0

Settings = json.load(open('Settings.json'))

intents, intents.members = discord.Intents.all(), True
client = commands.Bot(command_prefix=Settings['Prefix'],intents=intents)

def safePrint(member=None, action=None, vocab=None, color=None):
    return print(f"{Fore.WHITE}[{datetime.utcfromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')}] {Fore.MAGENTA}-{Fore.RESET} {member} [{color}{action} {Settings['vanityURL']} {vocab} status{Fore.RESET}]") if vocab!=None else print(f"{Fore.WHITE}[{datetime.utcfromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')}]{Fore.MAGENTA} - {Fore.RESET}{member} [{color}{action.title()}{Fore.RESET}]")


@client.event
async def on_ready():
    if Settings['botStatus'].lower() == "playing":
        try:
            if Settings['modeStatus'].lower() == "online":
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.online)
            elif Settings['modeStatus'].lower() == "dnd":
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.do_not_disturb)
            elif Settings['modeStatus'].lower() == "idle":
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.idle)
            elif Settings['modeStatus'].lower() == "offline":
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.offline)
            else:
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.online)
            safePrint(member="Bot",action=f"Status Update to ({Settings['botStatus']})",vocab=None,color=Fore.GREEN)
        except Exception as e:
            safePrint(member="Bot",action=f"Failed to update status to [Playing] ({Settings['botStatus']}) | Reason: {e}",vocab=None,color=Fore.RED)
    elif Settings['botStatus'].lower() == "streaming":
        try:
            await client.change_presence(activity=discord.Streaming(name=Settings['Status'], url="https://twitch.tv/DankoOfficial"))
            safePrint(member="Bot",action=f"Status Update to ({Settings['botStatus']})",vocab=None,color=Fore.GREEN)
        except Exception as e:
            safePrint(member="Bot",action=f"Failed to update status to [Streaming] ({Settings['botStatus']}) | Reason: {e}",vocab=None,color=Fore.RED)
    elif Settings['botStatus'].lower() == "listening":
        try:
            if Settings['modeStatus'].lower() == "online":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Settings['Status']),status=discord.Status.online)
            elif Settings['modeStatus'].lower() == "dnd":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Settings['Status']),status=discord.Status.do_not_disturb)
            elif Settings['modeStatus'].lower() == "idle":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Settings['Status']),status=discord.Status.idle)
            elif Settings['modeStatus'].lower() == "offline":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Settings['Status']),status=discord.Status.offline)
            else:
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Settings['Status']),status=discord.Status.online)
            safePrint(member="Bot",action=f"Failed to update status to [Listening] ({Settings['botStatus']}) | Reason: {e}",vocab=None,color=Fore.RED)
        except Exception as e:
            print(f"Failed to update status to [Listening] ({Settings['botStatus']}) | Reason: {e}")
    elif Settings['botStatus'].lower() == "watching":
        try:
            if Settings['modeStatus'].lower() == "online":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings['Status']),status=discord.Status.online)
            elif Settings['modeStatus'].lower() == "dnd":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings['Status']),status=discord.Status.do_not_disturb)
            elif Settings['modeStatus'].lower() == "idle":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings['Status']),status=discord.Status.idle)
            elif Settings['modeStatus'].lower() == "offline":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings['Status']),status=discord.Status.offline)
            else:
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings['Status']),status=discord.Status.online)
            safePrint(member="Bot",action=f"Status Update to ({Settings['botStatus']})",vocab=None,color=Fore.GREEN)
        except Exception as e:
            safePrint(member="Bot",action=f"Failed to update status to [Watching] ({Settings['botStatus']}) | Reason: {e}",vocab=None,color=Fore.RED)
    elif Settings['Status']!="":
        try:
            if Settings['modeStatus']!="":
                if Settings['modeStatus'].lower() == "online":
                    await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.online)
                elif Settings['modeStatus'].lower() == "dnd":
                    await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.do_not_disturb)
                elif Settings['modeStatus'].lower() == "idle":
                    await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.idle)
                elif Settings['modeStatus'].lower() == "offline":
                    await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.offline)
                else:
                    await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.online)
            else:
                await client.change_presence(activity=discord.Game(name=Settings['Status']),status=discord.Status.online)
            safePrint(member="Bot",action=f"Status Update to ({Settings['botStatus']})",vocab=None,color=Fore.GREEN)
        except Exception as e:
            safePrint(member="Bot",action=f"Failed to update status to [Playing] ({Settings['botStatus']}) | Reason: {e}",vocab=None,color=Fore.RED)
    else:
        safePrint(member="Bot",action=f"No status set, skipping...",vocab=None,color=Fore.YELLOW)
    
    channel = client.get_channel(Settings['channelLogs'])
    role = get(channel.guild.roles, name=Settings['roleName'])
    for member in channel.guild.members:
        if member.bot != True:
            try:
                if Settings['vanityURL'] in member.activities[0].name:
                    Status.roles+=1
                    if role not in member.roles:
                        await channel.send(embed=discord.Embed(title="Status Detected",description=f"{member.mention} has added {Settings['vanityURL']} in status. [{Settings['roleName']}](https://github.com/DankoOfficial) role added",colour=0x00FF00))
                        await member.add_roles(role)
                        safePrint(member=member,action="Added",vocab="in",color=Fore.GREEN)
                else:
                    if role in member.roles:
                        Status.roles-=1
                        await channel.send(embed=discord.Embed(title="Status Detected",description=f"{member.mention} has removed {Settings['vanityURL']} from status. [{Settings['roleName']}](https://github.com/DankoOfficial) role removed",colour=0xe60721))
                        await member.remove_roles(role)
                        safePrint(member=member,action="Removed",vocab="from",color=Fore.RED)
            except Exception as e:
                safePrint(member="Bot",action=f"Couldnt update {member} role, Error: {e}",color=Fore.YELLOW,vocab=None)
@client.event
async def on_member_update(before, after):
    channel = client.get_channel(Settings['channelLogs'])
    role = get(after.guild.roles, name=Settings['roleName'])
    if after.activities and Settings['vanityURL'] in after.activities[0].name:
        if role not in after.roles:
            Status.roles+=1
            await channel.send(embed=discord.Embed(title="Status Detected",description=f"{after.mention} has added {Settings['vanityURL']} in status. [{Settings['roleName']}](https://github.com/DankoOfficial) role added",colour=0x00FF00))
            try:
                await after.add_roles(role)
            except:
                safePrint(member=after,action="Failed to update Roles, Missing Permissions",vocab=None,color=Fore.LIGHTYELLOW_EX)
            safePrint(member=after,action="Added",vocab="in",color=Fore.GREEN)
    else:
        if role in after.roles:
            Status.roles-=1
            await after.remove_roles(role)
            await channel.send(embed=discord.Embed(title="Status Detected",description=f"{after.mention} has removed {Settings['vanityURL']} from status. [{Settings['roleName']}](https://github.com/DankoOfficial) role removed",colour=0xe60721))
            safePrint(member=after,action="Removed",vocab="from",color=Fore.RED)

@client.command()
async def status(ctx):
    await ctx.send(embed=discord.Embed(title=Settings['vanityURL'],description=f"There are {Status.roles} members that have [{Settings['vanityURL']}](https://github.com/DankoOfficial) in their status. (`{str(Status.roles)}`/`{str(len(ctx.guild.members))}`) | **{int(Status.roles)/int(len(ctx.guild.members))*100}%**",colour=0xe60721))

client.run(Settings['Token'])