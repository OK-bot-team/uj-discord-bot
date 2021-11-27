FROM gorialis/discord.py

WORKDIR /uj-discord-bot

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]