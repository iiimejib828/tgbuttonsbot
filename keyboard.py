from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

list = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/home')],
   [InlineKeyboardButton(text="Видео", url='https://vkvideo.ru/')],
   [InlineKeyboardButton(text="Новости", url='https://dzen.ru/news')]
])

async def show_more_kbd():
   keyboard = InlineKeyboardBuilder()
   keyboard.button(text="Показать больше", callback_data="show_more")
   return keyboard.adjust(2).as_markup()

async def choose_optn_kbd():
   keyboard = InlineKeyboardBuilder()
   keyboard.button(text="Опция 1", callback_data="option_1")
   keyboard.button(text="Опция 2", callback_data="option_2")
   return keyboard.adjust(2).as_markup()

