from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Главное меню ---------------------
btnTimetable = KeyboardButton('📆 Расписание')
btnPosts = KeyboardButton('📜 Посты с группы Computer-Center')
btnGeo = KeyboardButton('📍 Местоположение зданий университета')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnTimetable, btnPosts, btnGeo)

# ------------------- Получение постов VK ---------------------