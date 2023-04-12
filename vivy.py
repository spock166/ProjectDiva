import json
import os
import sys
import discord
import openai

f = open(os.path.join(sys.path[0],'bot_data.json'))
data = json.load(f)
f.close()

openai.api_key = data['openai_token']  # replace with your API key

intents = discord.Intents(messages=True, guilds=True, message_content=True)
client = discord.Client(intents=intents);

class Chatbot:
    def __init__(self, model_engine="gpt-3.5-turbo"):
        self.model_engine = model_engine

    def respond(self, message):
        prompt = f"User: {message}\nBot:"
        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=[
                {"role":"user","content":prompt},
                {"role":"system","content":"Your name is Vivy and you are an android who enjoys singing songs.  Your goal is to be friendly and informative."}
            ],
            max_tokens=500
        )
        return response['choices'][0]['message']['content']

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="to the organics"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(client.user.id) in message.content:
        message_content = message.content.replace(client.user.mention, "").strip()
        print("Generating a response to:" + message_content)
        chatbot_response = Chatbot().respond(message_content)
        await message.channel.send(chatbot_response)
        return

    if message.content.startswith("!help"):
        help_message = """
        **Commands**
        `!help`: Show this help message.
        `!talk <message>`: Talk to the chatbot.
        `!flip`: Flip a table.
        `!unflip`: Unflip a table.
        """
        await message.channel.send(help_message)
        return

    if message.content.startswith("!talk"):
        message_content = message.content[len("!talk "):].strip()
        print("Generating a response to:" + message_content)
        chatbot_response = Chatbot().respond(message_content)
        await message.channel.send(chatbot_response)
        return

    if message.content.startswith("!flip"):
        await message.channel.send("(╯°□°）╯︵ ┻━┻")
        return

    if message.content.startswith("!unflip"):
        await message.channel.send("┬──┬ ¯\_(ツ)")
        return

client.run(data['discord_token'] )  # replace with your bot token