<h1 align="center">Genie</h1>
<p align="center"><img src="https://github.com/tarranprior/genie/blob/main/assets/genie.png" /></p>

<p align="center">🧞 Genie is an open-source levelling and rewards system built for the Discord community, inspired by Old School RuneScape.</p>

<div align="center">

![GitHub License](https://img.shields.io/github/license/tarranprior/genie)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/tarranprior/genie)
![GitHub repo size](https://img.shields.io/github/repo-size/tarranprior/genie)
![GitHub forks](https://img.shields.io/github/forks/tarranprior/genie)
![GitHub Repo stars](https://img.shields.io/github/stars/tarranprior/genie)
![GitHub watchers](https://img.shields.io/github/watchers/tarranprior/genie)

</div>

## Features

## Usage

### Experience
The difference between *Level* $`L-1`$ and *Level* $`L`$ is <img src="https://github.com/tarranprior/genie/blob/main/assets/formula.png" />. The tables below show this experience difference for each level and also the cumulative experience from *Level 1* to *Level* $`L`$. 

## Tools

## Prerequisites

## Installation
Preferably, you should use Poetry to run this bot for local development:

1. Clone the repository. `git clone https://github.com/tarranprior/genie.git`
2. Navigate to the project folder. `cd genie`
3. Install the dependencies:

    ```s
    poetry install
    ```

    Alternatively, you can install the dependencies using pip:
    
    ```s
    pip install -r requirements.txt
    ```

## Setup
1. Create an application at [Discord Developer Portal](https://discord.com/developers/applications). Build a bot, and copy the token.
2. Invite the bot to your server.
3. Update the values in [Configuration](#configuration).
4. Run the bot:

    ```s
    poetry run python src/main.py
    ```

## Configuration
1. Update the values in `.env.EXAMPLE` and rename to `.env`.

   ```s
   BOT_TOKEN = 'YOUR_BOT_TOKEN'
   BOT_OWNER = 'YOUR_USER_ID'
   ```
2. *Optional*: Update the activity in `config.json`.

   ```json
   {
       "activity": "",
   }
   ```

## Disclaimer
RuneScape and RuneScape Old School are the trademarks of Jagex Limited and are used with the permission of Jagex.

## Support
If you have any questions about this project, please submit an issue [here](https://github.com/tarranprior/genie/issues).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/tarranprior/genie/blob/main/LICENSE) file for details.
