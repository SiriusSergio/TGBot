import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import user_handlers
from handlers import other_handlers

# init logger
logger = logging.getLogger(__name__)


# config and start bot
async def main():
    # congig logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    # output to console about start of the bot
    logging.info("Starting bot")

    # load config to variable
    config: Config = load_config()

    # init bot and dispatcher
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # registering routers
    logger.info("Registering routers")
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
