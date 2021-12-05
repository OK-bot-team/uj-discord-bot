FROM gorialis/discord.py

WORKDIR /uj-discord-bot

COPY . .

RUN pip install -U git+https://github.com/Pycord-Development/pycord
RUN pip install -r requirements.txt

CMD ["python", "run.py"]