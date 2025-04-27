#! /usr/bin/env python3

import asyncpg
import os, platform

from loguru import logger
import discord
from discord.ext import commands, tasks

from config import DATABASE_USERNAME, DATABASE_PASSWORD
from utils.database import initialise_database, populate_experience_table
from utils.helpers import configuration, experience_table


class Bot(commands.Bot):
    """
    A class which represents a Discord bot instance.
    """

    def __init__(self, config = None, *args, **kwargs) -> None:
        """
        Initialises a new instance of the Bot class.

        :param self: -
            Represents this object.
        :param config: (Optional[Dictionary]) -
            A dictionary containing configuration details.

        :return: (None)
        """

        super().__init__(*args, **kwargs)
        self.config = config or configuration()
        self.bot = Bot


    async def load_extensions(self, exts: list) -> None:
        """
        Loads all extensions (cogs) for the bot.

        :param self: -
            Represents this object.
        :param exts: (List) -
            A list of file paths for the extensions.

        :return: (None)
        """

        count = 0
        for ext in exts:
            try:
                await self.load_extension(ext)
                logger.success(f"Load ext: '{ext}' complete.")
                count += 1
            except Exception as e:
                exception = f'{type(e).__name__}: {e}'
                logger.error(f"Unable to load extension: {ext}\n{exception}.")

        logger.info(f"{count} extension(s) have loaded successfully.\n")


    async def on_connect(self) -> None:
        """
        A coroutine that is called when the bot has connected to
        the Discord gateway.

        :param self: -
            Represents this object.

        :return: (None)
        """

        logger.success("Genie is connected to the gateway.")
        logger.info(f"Logged in as {self.user.name} ({self.user.id})")
        logger.info(f"API Version: {discord.__version__}")
        logger.info(f"Platform: {platform.system()} {platform.release()} {os.name}\n")

        self.database = await asyncpg.create_pool(
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
            database="GENIEDB",
            host="localhost", # Default Host
            port=5432 # Default Port
        )

        await initialise_database(self)
        await populate_experience_table(self, experience_table())


    async def on_ready(self) -> None:
        """
        A coroutine that executes when the bot is fully initialised
        and ready to respond to events.

        :param self: -
            Represents this object.

        :return: (None)
        """

        logger.success("Genie is ready.")
        logger.info("For more information on usage, see the README.")


    async def on_slash_command_error(
        self,
        inter: discord.Interaction,
        error: Exception
    ) -> None:
        """
        A coroutine that is called when a slash command encounters
        an error.

        :param self: -
            Represents this object.
        :param inter: (ApplicationCommandInteraction) -
            The interaction that resulted in the error.
        :param error: (Exception) -
            The error that was raised.

        :return: (None)
        """
    
        logger.error(f"Ignoring exception in slash command {inter.application_command.name}: {error}")


    @tasks.loop(minutes=10.0)
    async def status() -> None:
        await Bot.change_presence(
            activity=discord.Game(
                name=Bot.config["configuration"]["activity"]
            )
        )
