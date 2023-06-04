from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.misc import replicas, keyboards
from tgbot.misc.location import Location
from tgbot.misc.place_text import get_place_text
from tgbot.misc.spotter import NearSpotter
from tgbot.misc.states import FindSG
from tgbot.models import Place

find_router = Router()


@find_router.message(Command("find"))
async def find(message: Message, state: FSMContext):
    await message.answer(text=replicas.find.substitute(), reply_markup=keyboards.find)
    await state.set_state(FindSG.location)


@find_router.message(FindSG.location, F.content_type == 'text')
async def take_not_location(message: Message):
    await message.answer(text=replicas.find.substitute(), reply_markup=keyboards.find)


@find_router.message(FindSG.location, F.content_type.in_(['location']))
async def take_location(message: Message, state: FSMContext):
    location = Location(message.location)
    spotter = NearSpotter(batch_size=1)
    spotter.generate(location)
    await state.update_data(spotter=spotter)
    await send_places(message, state)


@find_router.callback_query(FindSG.next_places, Text('next'))
async def next_places(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=callback.message.text)
    await send_places(callback.message, state)


async def send_places(message: Message, state: FSMContext):
    spotter = (await state.get_data())['spotter']
    meta_places = next(spotter, "STOP")

    if meta_places != "STOP":
        for meta_place in meta_places:
            place = Place.objects.get(pk=meta_place.place_id)
            text = get_place_text(place=place, meta_place=meta_place)
            await message.answer(text=text, reply_markup=keyboards.places, disable_web_page_preview=True)

        await state.set_state(FindSG.next_places)

    else:
        await message.answer('Все! Пизда тачке, снимай колеса. Больше мест у меня нет')
        await state.clear()
