import disnake as discord
from api import *
from config import maloja_endpoint, maloja_apikey

def remove_prefix(text, prefix):
    return text.lstrip(prefix).upper()

async def process_command(message, prefix):
    if remove_prefix(message.content, prefix) == "R":
        scrobbles = await grab_scrobbles(maloja_endpoint)
        r = recent(scrobbles)
        embed = discord.Embed(
            title="Most Recent",
            description=", ".join(r['track']['artists']) + " - " + r['track']['title'],
            color=discord.Color.random(),
        )
        embed.set_footer(
            text="Requested by " + message.author.display_name,
            icon_url="https://raw.githubusercontent.com/krateng/maloja/master/maloja/web/static/png/favicon.png",
        )
        await message.channel.send(embed=embed)