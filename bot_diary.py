import logging
import os
import markup as nav

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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)