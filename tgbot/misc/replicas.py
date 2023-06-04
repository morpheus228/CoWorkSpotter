from string import Template


start = Template('Здоров, мен! Здесь ты можешь найти ближашие места, '
                 'где ты можешь поработать и поучиться.'
                 'Чтобы начать нажми кнопку /find')

find = Template('Отправь свое местоположение!')


place = Template('$sml1 <b>$name</b> $sml2\n\n'
                 '<i>$desc</i>\n\n'
                 '<a href="$url">🔗Ссылка на сайт</a>\n\n'
                 '📅🕑Часы работы: <i>$w_h</i>\n\n'
                 'Расстояние до вас: <i>$distance</i>\n'
                 '<a href="$ymap">📍Открыть в Яндекс Картах</a>\n\n')
