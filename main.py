from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
from random import choice
from ServerManager import TOKEN
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot = Bot(token=TOKEN)
dp = Dispatcher()

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Сайт", url="https://example.com")],
    [InlineKeyboardButton(text="✉️ Информация", callback_data="info")],
    [InlineKeyboardButton(text="⚒️ Чат-бот", callback_data="bot")],
    [InlineKeyboardButton(text="⛔️ Фото по ссылке (Нету функции)⛔️", callback_data="photo")]
])


@dp.message(Command("start"))
async def h_start(message: types.Message):
    photo = FSInputFile("SimonLogo.png")
    await message.answer_photo(photo=photo, caption=(
                f"Привет, {message.from_user.username}! 👋\n\n"
                "Этот бот может:\n"
                "• Отправить информацию о вашем аккаунте.\n"
                "• Функция чат-бота (в разработке 🤖)\n"
                "• Отправить фото по ссылке.\n"
                "• Играть с вами в игру 'Игра дня' 🎮\n\n"
                "Нажмите на кнопку и выберите функцию из списка."
    ), reply_markup=inline_kb)


@dp.message(Command("plane"))
async def plane_promo(message: types.Message):
    await message.answer(f"Поздравляем, @{message.from_user.username}")
    text = (
            "<blockquote>"
            f"<b>Поздравляем, @{message.from_user.username}</b>"
            f"<b>Вы ввели секретную команду и были добавлены в список участников!</b>"
            "</blockquote>"
        )

    await bot.send_message(message.from_user.id, text, parse_mode="HTML")


#### FULL SCRIPT - YOU NEED BUY
