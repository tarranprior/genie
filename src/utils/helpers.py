#! /usr/bin/env python3

import json
import os, sys


def configuration() -> dict:
    """
    Helper function which reads the configuration file (config.json)
    and returns its contents as a dictionary.

    :return: (Dictionary) -
        A dictionary representing the contents of the configuration file.
    """
    
    if os.path.isfile("config.json"):
        with open("config.json") as json_file:
            data = json.load(json_file)
            return data
    else:
        sys.exit(f"Configuration file not found. Please add it and try again.")


def experience_table() -> dict:
    """
    Helper function which reads the experience table (xp_table.json)
    and returns its contents as a dictionary.

    :return: (List) -
        A dictionary representing the contents of the experience table.
    """

    if os.path.isfile("xp_table.json"):
        with open("xp_table.json", encoding="utf-8") as json_data:
            experience_table = json.load(json_data)
            return experience_table["experience_table"]
    else:
        sys.exit("Experience table not found.")
