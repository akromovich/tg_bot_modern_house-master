from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
k_1 = KeyboardButton('A')
k_2 = KeyboardButton('Б')
k_3 = KeyboardButton('В')
k_4 = KeyboardButton('Г')
kb.add(k_1,k_2,k_3,k_4)
