import discord
import csv
import pandas as pd
TOKEN = 'NTIwMDg2OTkzODM3ODgzNDI4.DzTLgg.FhmoMxFzR4A0F1AGlLgy1E74CNk'

client = discord.Client()

f = open('Untitled spreadsheet - Sheet1.csv')
read = csv.reader(f)

print('-------------')
print('Under 10')
df = pd.read_csv('Untitled spreadsheet - Sheet1.csv')

under_10 = df['Highest']<10

df_high = df[under_10]

print(df[df.Highest < 10])

hf = df[df.Highest < 10]

print('------------------')


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!test'):
		msg = 'you suck'.format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('----------');

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        if message.content.startswith('!10'):
		msg = hf.format(message)
                await client.send_message(message.channel, msg)


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!asd'):
		msg = 'get trolled'.format(message)
		await client.send_message(message.channel, msg)			
	
client.run(TOKEN);

