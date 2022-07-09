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
        await bot.send_message(message.from_user.id, "В разработке")
    elif message.text == '📍 Местоположение зданий университета':
        await bot.send_message(message.from_user.id, "Выберите нужное вам здание:", reply_markup=nav.buildingMenu)
    elif message.text == "Первое":
        await bot.send_message(message.from_user.id, "Первое здание КАИ📍\n"
                                                     "Адрес: Карла Маркса, 10", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.797054, 49.114090)
    elif message.text == "Второе":
        await bot.send_message(message.from_user.id, "Второе здание КАИ📍\n"
                                                     "Адрес: Четаева, 18", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.82265, 49.13606)
    elif message.text == "Третье":
        await bot.send_message(message.from_user.id, "Третье здание КАИ📍\n"
                                                     "Адрес: Льва Толстого, 15", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.79226, 49.13748)
    elif message.text == "Четвертое":
        await bot.send_message(message.from_user.id, "Четвертое здание КАИ📍\n"
                                                     "Адрес: Льва Толстого, 17", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.7932, 49.13739)
    elif message.text == "Пятое":
        await bot.send_message(message.from_user.id, "Пятое здание КАИ📍\n"
                                                     "Адрес: Карла Маркса, 31", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.79654, 49.12387)
    elif message.text == "Шестое":
        await bot.send_message(message.from_user.id, "Шестое здание КАИ📍\n"
                                                     "Адрес: Дементьева, 2А", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.85416, 49.09821)
    elif message.text == "Седьмое":
        await bot.send_message(message.from_user.id, "Седьмое здание КАИ📍\n"
                                                     "Адрес: Большая Красная, 55", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.79692, 49.13392)
    elif message.text == "Восьмое":
        await bot.send_message(message.from_user.id, "Восьмое здание КАИ📍\n"
                                                     "Адрес: Четаева, 18А", reply_markup=nav.mainMenu)
        await bot.send_location(message.from_user.id, 55.82089, 49.13627)
    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, "Жаль, что ты не выбрал😥", reply_markup=nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)