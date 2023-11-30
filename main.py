import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram_dialog.setup import setup_dialogs

from bot.dialogs.opt_menu.setup import bot_opt_menu
from bot.handlers import router_list
from config import Config


async def startup(bot: Bot):
    for admin_id in Config.ADMINS:
        await bot.send_message(admin_id, "Бот был запущен!")


async def main():
    bot = Bot(token=Config.TOKEN)
    dp = Dispatcher()

    dp.include_routers(*bot_opt_menu())
    dp.include_routers(*router_list)
    setup_dialogs(dp)

    await startup(bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
