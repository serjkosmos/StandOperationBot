from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/Первый_ящик')
b2 = KeyboardButton('/Термины')
b3 = KeyboardButton('/Профиль')
b4 = KeyboardButton('/5s')
b5 = KeyboardButton('/Критерии_паллета')
b6 = KeyboardButton('/Контроль_качества')
b7 = KeyboardButton('/Охрана_труда')
b8 = KeyboardButton('/Выборка')
b9 = KeyboardButton('/Отклонения')
# b5 = KeyboardButton('my adress', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2).row(b3, b4).row(b5, b6).row(b7, b8).add(b9)