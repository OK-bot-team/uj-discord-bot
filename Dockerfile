FROM gorialis/discord.py

WORKDIR /uj-discord-bot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]