from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Главное меню ---------------------
btnTimetable = KeyboardButton('📆 Расписание')
btnPosts = KeyboardButton('📜 Посты с группы Computer-Center')
btnGeo = KeyboardButton('📍 Местоположение зданий университета')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnTimetable, btnPosts, btnGeo)

# ------------------- Получение постов VK ---------------------

btnFirst = KeyboardButton("Первое")
btnSecond = KeyboardButton("Второе")
btnThird = KeyboardButton("Третье")
btnFourth = KeyboardButton("Четвертое")
btnFifth = KeyboardButton("Пятое")
btnSixth = KeyboardButton("Шестое")
btnSeventh = KeyboardButton("Седьмое")
btnEighth = KeyboardButton("Восьмое")
btnAgain = KeyboardButton("Назад")

buildingMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFirst, btnSecond, btnThird, btnFourth, btnFifth, btnSixth, btnSeventh, btnEighth, btnAgain)