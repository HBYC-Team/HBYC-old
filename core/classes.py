from http import client
import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, client):
        self.client = client