from aiogram import Bot,Dispatcher,executor,types
from aiohttp import web
from handlers import admin
from create_bot import dp,bot

async def on_startup(_):
    print('BOT:ONLINE')

admin.register_handlers_admin(dp)

executor.start_polling(dp,skip_updates=True,on_startup=on_startup)