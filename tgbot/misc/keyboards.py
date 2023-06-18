from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

remove = ReplyKeyboardRemove()

find = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📍 Отправить своё местоположение', request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True)

places = InlineKeyboardBuilder([
        [
            InlineKeyboardButton(
                text="Подробнее о месте",
                url='https://telegra.ph/Kovorking-Tochka-kipeniya-06-07-3'
            )
         ],
        [
            InlineKeyboardButton(
                text="Следующие место ⏭",
                callback_data="next"
            )
        ]
    ]).as_markup()

places_short = InlineKeyboardBuilder([
        [
            InlineKeyboardButton(
                text="Подробнее о месте",
                url='https://telegra.ph/Kovorking-Tochka-kipeniya-06-07-3'
            )
         ]
    ]).as_markup()


