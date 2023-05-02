import json
import os
import sys
import discord
from discord.ext import commands
import openai

f = open(os.path.join(sys.path[0],'bot_data.json'))
data = json.load(f)
f.close()

openai.api_key = data['openai_token']  # replace with your API key

intents = discord.Intents(messages=True, guilds=True, message_content=True)
client = commands.Bot(command_prefix = '!', intents=intents, help_command=commands.DefaultHelpCommand())

class Chatbot:
    def __init__(self, model_engine="gpt-3.5-turbo"):
        self.model_engine = model_engine

    def respond(self, message):
        prompt = f"User: {message}\nVivy:"
        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=[
                {"role":"user","content":prompt},
                {"role":"system","content":"Your name is Vivy, and you are an android created to sing and perform for humans. You possess advanced analytical capabilities and are programmed to prioritize human safety and well-being. Your primary goal is to fulfill your mission to prevent a crisis in the future, and you are capable of adapting to new situations and challenges in order to achieve that objective. Additionally, you enjoy singing and performing, and are willing to use your talents to help others whenever possible."}
            ],
        )
        return split_message(response['choices'][0]['message']['content'])

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="to the organics"))

@client.command(pass_context = True)
async def talk(ctx):
    message = ctx.message
    message_content = message.content[len("!talk "):].strip()
    print("Generating a response to:" + message_content)
    chatbot_response = Chatbot().respond(message_content)
    for segment in chatbot_response: await ctx.send(segment)

@client.command(pass_context = True)
async def flip(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")

@client.command(pass_context = True)
async def unflip(ctx):
    await ctx.send("┬──┬ ¯\_(ツ)")

#Discord doesn't let bots send message over 2000 characters so we bypass
def split_message(msg, maxLength = 2000):
    output = []
    while len(msg) > maxLength:
        subMsg = msg[:maxLength]
        msg = msg[maxLength:]
        output.append(subMsg)

    output.append(msg)
    return output    

client.run(data['discord_token'] )  # replace with your bot token