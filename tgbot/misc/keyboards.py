from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

remove = ReplyKeyboardRemove()

find = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📍 Отправить своё местоположение', request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=False)

places = InlineKeyboardBuilder([
        [
            InlineKeyboardButton(
                text="Следующие место ⏭",
                callback_data="next"
            )
         ]
    ]).as_markup()


