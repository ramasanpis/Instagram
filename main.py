from logger_config import logger
from queue_db import init_db
from telegram_bot import IGBot

def main():
    init_db()
    bot = IGBot()
    try:
        bot.run()
    except KeyboardInterrupt:
        logger.info("Shutting down.")

if __name__ == "__main__":
    main()
