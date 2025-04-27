<h1 align="center">RuneScape Levels</h1>
<p align="center">An open-source levelling and rewards system built for the Discord community, inspired by Old School RuneScape.</p>

<div align="center">

![GitHub License](https://img.shields.io/github/license/tarranprior/runescape-levels)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/tarranprior/runescape-levels)
![GitHub repo size](https://img.shields.io/github/repo-size/tarranprior/runescape-levels)
![GitHub forks](https://img.shields.io/github/forks/tarranprior/runescape-levels)
![GitHub Repo stars](https://img.shields.io/github/stars/tarranprior/runescape-levels)
![GitHub watchers](https://img.shields.io/github/watchers/tarranprior/runescape-levels)

</div>

## Features

## Usage

### Experience

The difference between *Level* $`L-1`$ and *Level* $`L`$ is $`\frac{1}{4}\left(L-1+300\cdot2\frac{(L-1)}{7}\right)`$. To calculate the amount of experience needed to reach *Level* $`L`$:

$`Experience`$ = $`\left(\frac{1}{4}\displaystyle\sum_{\ell=1}^{L-1}\left(\ell+300\cdot2^{\ell/7}\right)\right)`$

The following summation simplifies to the closed-form expression if floor functions are ignored:

$`Experience`$ ≈ $`\frac{1}{8}\left(L^2-L+600\frac{2^{L/7}-2^{1/7}}{2^{1/7}-1}\right)`$

The approximation is very accurate, always being within 14 experience of the true value. One of the final approximations is:

$`Experience`$ ≈ $`\frac{1}{8}\left(L^2-L+600\frac{2^{L/7}-2^{1/7}}{2^{1/7}-1}\right)-\frac{L}{10}-γ=\frac{L^{2}}{8}-\frac{9}{40}L+75\frac{2^{L/7}-2^{1/7}}{2^{1/7}-1}-γ`$

where $`γ`$ is the [Euler–Mascheroni constant](https://en.wikipedia.org/wiki/Euler%27s_constant). This approximation always gives an answer within 1 experience of the true value. 

### Experience table

`xp_table.json` shows this experience difference for each level, as well as the cumulative experience from *Level 1* to *Level* $`L`$.

```json
    {
      "level": 1,
      "total_experience": 0,
      "experience_difference": null
    },
    {
      "level": 2,
      "total_experience": 83,
      "experience_difference": 83
    },
    {
      "level": 3,
      "total_experience": 174,
      "experience_difference": 91
    },
    {
      "level": 4,
      "total_experience": 276,
      "experience_difference": 102
    },
    {
      "level": 5,
      "total_experience": 388,
      "experience_difference": 112
    },
    "_comment": "...",
```

RuneScape levels cap at *Level* $`99`$, so we use "virtual" levels to track XP above the level cap. These levels are also written in `xp_table.json`.

```json
    {
      "level": 100,
      "total_experience": 14391160,
      "experience_difference": 1356729
    },
    {
      "level": 101,
      "total_experience": 15889109,
      "experience_difference": 1497949
    },
    {
      "level": 102,
      "total_experience": 17542976,
      "experience_difference": 1635867
    },
    {
      "level": 103,
      "total_experience": 19368992,
      "experience_difference": 1826016
    },
    {
      "level": 104,
      "total_experience": 21385073,
      "experience_difference": 2016081
    },
    "_comment": "...",
```

## Prerequisites

* Python 3.11 +
* [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool).
* [PostgreSQL](https://www.postgresql.org/)

## Tools

* [Discord.py](https://github.com/Rapptz/discord.py)
* [asyncpg](https://github.com/MagicStack/asyncpg)
* [Loguru](https://github.com/Delgan/loguru)
* [Python-dotenv](https://github.com/theskumar/python-dotenv)

## Installation
Use [Poetry](https://python-poetry.org/) to run this bot for local development:

1. Clone the repository. `git clone https://github.com/tarranprior/genie.git`
2. Navigate to the project folder. `cd genie`
3. Install the dependencies:

    ```s
    poetry install
    ```

    You can also install the dependencies using pip:
    
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
   DATABASE_USERNAME = 'YOUR_DATABASE_USERNAME'
   DATABASE_PASSWORD = 'YOUR_DATABASE_PASSWORD'
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
If you have any questions about this project, please submit an issue [here](https://github.com/tarranprior/runescape-levels/issues).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/tarranprior/runescape-levels/blob/main/LICENSE) file for details.
