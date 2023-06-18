from string import Template


start = Template('Здоров, мен! Здесь ты можешь найти ближашие места, '
                 'где ты можешь поработать и поучиться.'
                 'Чтобы начать нажми кнопку /find')

find = Template('Отправь свое местоположение!')


place = Template('$sml1 <b>$name</b> $sml2\n\n'
                 '<i>$desc</i>\n\n'
                 '🔗 <a href="$url">Ссылка</a>\n\n'
                 '🕑 $w_h\n\n'
                 '📍 Расстояние до вас: $distance км\n'
                 '🗺️ <a href="$ymaps">Открыть на картах</a>')
