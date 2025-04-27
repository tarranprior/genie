#! /usr/bin/env python3

import sys
sys.dont_write_bytecode = True

import asyncio

from contextlib import suppress
import discord
from discord.ext import commands

from config import BOT_OWNER, BOT_TOKEN
from templates.bot import Bot
from utils.helpers import configuration


if __name__ == "__main__":

    bot = Bot(
        activity=discord.Game(
            name=configuration()["configuration"]["activity"]
        ),
        command_prefix=commands.when_mentioned,
        intents=discord.Intents.all(),
        owner_id=BOT_OWNER
    )

    async def main():
        await bot.load_extensions([
        ])
        await bot.start(BOT_TOKEN)

    with suppress(KeyboardInterrupt):
        asyncio.run(main())
