from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

remove = ReplyKeyboardRemove()

find = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📍 Отправить своё местоположение', request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=False)
