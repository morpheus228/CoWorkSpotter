from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from tgbot.misc import replicas, keyboards
from tgbot.misc.funcs import NearSpotter, Coords
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
    await message.answer(str(spotter.get_places(location)))
    #location = (message.location.latitude, message.location.longitude)
    # await message.answer(text=replicas.place.substitute(), disable_web_page_preview=True, reply_markup=keyboards.remove)