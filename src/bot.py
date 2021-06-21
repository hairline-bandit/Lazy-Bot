import discord

LINK_GOOGLE = "https://www.google.com/search?q="
LINK_WOLFRAM = "https://www.wolframalpha.com/input/?i="

TOKEN = ""

client = discord.Client()

def rplace(msg):
    return msg.replace("+", "%2B")

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if message.content.strip().lower().startswith("google"):
        channel = message.channel
        await channel.send(LINK_GOOGLE + "+".join(rplace(" ".join(message.content.split(" ")[1:])).split(" ")))
    elif message.content.strip().lower().startswith("math"):
        channel = message.channel
        await channel.send(LINK_WOLFRAM + "+".join(rplace(" ".join(message.content.split(" ")[1:])).split(" ")))

client.run(TOKEN)
