# 🆗Bot 
[![Tests](https://github.com/Trenek/uj-discord-bot/actions/workflows/Tests.yml/badge.svg)](https://github.com/Trenek/uj-discord-bot/actions/workflows/Tests.yml)
![License](https://img.shields.io/github/license/OK-bot-team/uj-discord-bot)
![Black](https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-squar)
![TopLanguage](https://img.shields.io/github/languages/top/OK-bot-team/uj-discord-bot)

## Installation

You need to have uv installed. 

Clone the repository to your machine
```
git clone https://github.com/OK-bot-team/uj-discord-bot.git
```
or using ssh
```
git clone git@github.com:OK-bot-team/uj-discord-bot.git
```

Create necessary environment variables in repository, for example with .env file. Example file:
```
API_URL=<API_BACKEND_URL>
DISCORD_TOKEN=<YOUR-DISCORD-BOT-TOKEN>
```


Synchronize your enviroment using uv
```
uv sync
```
Now u can successfully run the bot with the following command
```
uv run run.py
```

## Testing ✔️
Testing is done with pytest framework. 

to run pytest tests:
```
uv run pytest
```

to add more tests, create them in tests directory in compliance to [pytest documentation](https://docs.pytest.org/en/6.2.x/example/index.html).
