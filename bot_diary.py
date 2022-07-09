import logging
import os
import markup as nav
import vk_init
from vk_init import *

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('access_token')

# Configure logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f"📬Привет, {message.from_user.first_name}\n\n"
                        f"Здесь ты можешь найти актуальную информацию🔎\n\n"
                        f"📆 О расписании\n"
                        f"📜 Посты с группы Computer-Center\n"
                        f"📍 Местоположение зданий университета", reply_markup=nav.mainMenu)

@dp.message_handler()
async def echo(message: types.Message):
    if(message.text == '📆 Расписание'):
        await bot.send_message(message.from_user.id, 'Здесь должно быть расписание')
    elif message.text == '📜 Посты с группы Computer-Center':
        vk_init.get_wall_posts()
        await bot.send_message(message.from_user.id, vk_init.get_wall_posts())
    elif message.text == '📍 Местоположение зданий университета':
        await bot.send_message(message.from_user.id, 'Здесь должны быть здания универа')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)