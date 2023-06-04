from string import Template

from tgbot.misc.funcs import NearSpotter, Coords

from aiogram.types import Message

start = Template('Здоров, мен! Здесь ты можешь найти ближашие места, '
                 'где ты можешь поработать и поучиться.'
                 'Чтобы начать нажми кнопку /find')

find = Template('Отправь свое местоположение!')

post_place = Template('$name\n$desc\n$url\n$w_h\n$ymap')
