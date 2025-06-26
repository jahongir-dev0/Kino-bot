from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.db_api.database import setup_tables
from utils.logger import notify_admins
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await notify_admins(dispatcher)
    setup_tables()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
