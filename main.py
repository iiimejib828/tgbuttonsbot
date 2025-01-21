import asyncio

from aiogram.utils.keyboard import InlineKeyboardBuilder

import keyboard as kb

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=kb.main)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/list\n/dynamic")

@dp.message(Command('list'))
async def list(message: Message):
    await message.answer(f"{message.from_user.first_name}, ты хочешь музыку, видео или новости?",
                         reply_markup=kb.list)

@dp.message(F.text == "Привет")
async def hello_button(message: Message):
   await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def bye_button(message: Message):
   await message.answer(f"Пока, {message.from_user.first_name}!")

@dp.message(Command("dynamic"))
async def send_dynamic_buttons(message: Message):
    await message.answer("Выберите опцию:", reply_markup=await kb.show_more_kbd())

@dp.callback_query(F.data == "show_more")
async def show_more_options(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выберите опцию:", reply_markup=await kb.choose_optn_kbd())

@dp.callback_query(F.data.startswith("option_"))
async def option_selected(callback_query: CallbackQuery):
    option = "Опция 1" if callback_query.data == "option_1" else "Опция 2"
    await callback_query.message.answer(f"Вы выбрали: {option}")
    await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())