import os
from dotenv import load_dotenv

from src.discord_bot.bot import bot

load_dotenv()  # Load environment variables from .env file


def main():
    bot.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    main()
