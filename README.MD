# 🆗Bot 
![Build](https://img.shields.io/github/workflow/status/OK-bot-team/uj-discord-bot/Tests) 
![License](https://img.shields.io/github/license/OK-bot-team/uj-discord-bot)
![Black](https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-squar)
![TopLanguage](https://img.shields.io/github/languages/top/OK-bot-team/uj-discord-bot)

## Installation

You need to have [Docker](https://docs.docker.com/get-docker/) software installed. 

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
API_URL=<API_BACKED_URL>
DISCORD_TOKEN=<YOUR-DISCORD-BOT-TOKEN>
```


Build `docker` image in repository
```
docker build -t <your-image-name> <path-to-respository>
```
You can run the bot with your image name
```
docker run <your-image-name>
```
Example:
```
docker build -t ok-bot .
docker run -d ok-bot
```

## Testing ✔️
Testing is done with pytest framework. 

to run pytest tests:
```
pytest <path-to-repository>
```

to add more tests, create them in tests directory in compliance to [pytest documentation](https://docs.pytest.org/en/6.2.x/example/index.html).
