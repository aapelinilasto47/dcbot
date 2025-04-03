import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.run('MTMzMDg2NDE2MDUyNzA5Mzg5Mw.GodYfg.DfS82AHQ3C73-q6Gi9XESJr5gOZavLUz50oZ1g')

