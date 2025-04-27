#! /usr/bin/env python3

from os import environ as env
from dotenv import load_dotenv


load_dotenv()

BOT_OWNER = int(env["BOT_OWNER"])
BOT_TOKEN = str(env["BOT_TOKEN"])

DATABASE_USERNAME = str(env["DATABASE_USERNAME"])
DATABASE_PASSWORD = str(env["DATABASE_PASSWORD"])
