import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import ball
import asyncio

BOT_TOKEN = os.environ["BOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"We're logged in as {bot.user}!")
    await bot.tree.sync()


@bot.tree.command(name="ask", description="Ask the magic 8 ball a question")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    reply = ball.get_response(question)
    await asyncio.sleep(1)
    await interaction.followup.send(reply) 


bot.run(BOT_TOKEN)
