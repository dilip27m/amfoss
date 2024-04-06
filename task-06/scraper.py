import io
import requests
from bs4 import BeautifulSoup
import csv
import dotenv
import discord
from dotenv import load_dotenv
from datetime import datetime
from io import StringIO
from discord.ext import commands
import os
import aiohttp
from io import StringIO
load_dotenv()
discord_id = os.getenv('discord_id')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
# Function to scrape live cricket score
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Define scraping function

async def scrape_live_scores():
    url = "https://www.espncricinfo.com/live-cricket-score"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), 'html.parser')

                team1 = soup.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
                team2 = soup.find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
                score1 = soup.find('span', class_='ds-text-compact-xs ds-mr-0.5')
                score2 = soup.find('span', class_='ds-text-compact-xs ds-mr-0.5')
                summary = soup.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')

                if all((team1, team2, score1, score2, summary)):
                    return f"Team 1: {team1.text.strip()} {score1.text.strip()}\n" \
                           f"Team 2: {team2.text.strip()} {score2.text.strip()}\n" \
                           f"Match Summary: {summary.text.strip()}"
                else:
                    return "One or more elements not found. Check class names or HTML structure."
            else:
                return f"Failed to fetch data. Status code: {response.status}"


# Define bot commands
@bot.command(name='livescore', help='Get live feed on the crux of the match.')
async def get_live_score(ctx):
    live_score = await scrape_live_scores()
    await ctx.send(live_score)

@bot.command(name='generate', help='Get the CSV file containing live scores and timestamps.')
async def generate_csv(ctx):
    csv_data = "Timestamp,Team 1,Team 2,Match Summary\n" \
               f"{datetime.now()},Team1Name,Team2Name,MatchSummary\n"
    await ctx.send(file=discord.File(StringIO(csv_data), filename='live_scores.csv'))

# Define bot help command
@bot.command(name='bot_help', help='Get a list of commands along with their description.')
async def get_bot_help(ctx):
    help_message = "/livescore - Get live feed on the crux of the match.\n" \
                   "/generate - Get the CSV file containing live scores and timestamps.\n" \
                   "/bot_help - Get a list of commands along with their description."
    await ctx.send(help_message)
bot.run('MTIwODA5MDIzNTMyNjQzMTI2Mg.G_eJU-.HFvqzdrQaWB7mieZfpVGGNt7ZCbpScMH0a8LXc')