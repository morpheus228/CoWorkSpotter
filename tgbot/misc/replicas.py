from string import Template

from tgbot.misc.funcs import NearSpotter, Coords

from aiogram.types import Message

from aiogram.utils import markdown

start = Template('Здоров, мен! Здесь ты можешь найти ближашие места, '
                 'где ты можешь поработать и поучиться.'
                 'Чтобы начать нажми кнопку /find')

find = Template('Отправь свое местоположение!')

post_cowork = Template('📖' + markdown.hbold('$name') + '💻\n\n' + markdown.hitalic('$desc') + '\n\n' +
                       markdown.hlink(title='🔗Ссылка на сайт', url='$url') + '\n\n' + '📅🕑Часы работы:\n\n' +
                       markdown.hitalic('$w_h\n\n') + markdown.hlink(title='📍Открыть в Яндекс Картах', url='$ymap'))

post_food = Template('🍕' + markdown.hbold('$name') + '🍵\n\n' + markdown.hitalic('$desc') + '\n\n' +
                     markdown.hlink(title='🔗Ссылка на сайт', url='$url') + '\n\n' + '📅🕑Часы работы:\n\n' +
                     markdown.hitalic('$w_h\n\n') + markdown.hlink(title='📍Открыть в Яндекс Картах', url='$ymap'))
