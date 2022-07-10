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
btnAgain = KeyboardButton("Главное меню")

buildingMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFirst, btnSecond, btnThird, btnFourth, btnFifth, btnSixth, btnSeventh, btnEighth, btnAgain)

# ------------------ Расписание по курсам и группам -----------

btnCourse1 = KeyboardButton("1 курс")
btnCourse2 = KeyboardButton("2 курс")
btnCourse3 = KeyboardButton("3 курс")
btnCourse4 = KeyboardButton("4 курс")

courseMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnCourse1, btnCourse2, btnCourse3, btnCourse4)