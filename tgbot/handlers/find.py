from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from tgbot.misc import replicas, keyboards
from tgbot.misc.funcs import NearSpotter, Coords, places_all_info
from tgbot.misc.states import FindSG

find_router = Router()


@find_router.message(Command("find"))
async def find(message: Message, state: FSMContext):
    await message.answer(text=replicas.find.substitute(), reply_markup=keyboards.find)
    await state.set_state(FindSG.location)


@find_router.message(FindSG.location, F.content_type == 'text')
async def take_not_location(message: Message):
    await message.answer(text=replicas.find.substitute(), reply_markup=keyboards.find)


@find_router.message(FindSG.location, F.content_type.in_(['location']))
async def take_location(message: Message):
    spotter = NearSpotter()
    location = Coords(message.location.latitude, message.location.longitude)
    places = spotter.get_places(location)
    for place in places_all_info(places):
        post = replicas.post_place.substitute(name=place.name, desc=place.description, url=place.url,
                                              w_h=place.working_hours, ymap=place.ymap)
        await message.answer(text=post, disable_web_page_preview=True, reply_markup=keyboards.remove)
