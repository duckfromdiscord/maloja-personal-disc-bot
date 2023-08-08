import disnake as discord
import io
from config import discord_api_key, user_id, prefix
from commands import process_command

class MalojaBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.id != user_id:
            # Ignore queries from other users
            return
        if message.author == self.user:
            # Ignore own messages
            return
        if message.content.startswith(prefix):
            await process_command(message, prefix)



intents = discord.Intents.default()
intents.guild_messages = True
intents.message_content = True
client = MalojaBotClient(intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="bangers"))
client.run(discord_api_key)