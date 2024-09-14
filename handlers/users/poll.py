from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.poll_info import PollInfo


@dp.message_handler(Command('poll'))
async def poll_cmd(message: types.Message):
    await message.answer('Добро пожаловать в опросник!\n'
                         "Первый вопрос.\n\n"
                         'Нравится ли вам программировать?')
    await PollInfo.q_1.set()


@dp.message_handler(state=PollInfo.q_1)
async def get_frst_ans(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {
            'q_1': answer
        }
    )

    await message.answer('Второй вопрос\n\n'
                         'Сколько часов в день вы спите?')

    await PollInfo.q_2.set()


@dp.message_handler(state=PollInfo.q_2)
async def question_two(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            "q_2": text
        }
    )

    await message.answer('Третий вопрос\n\n'
                         'Сколько часов вы проводите за экранами?')

    await PollInfo.q_3.set()


@dp.message_handler(state=PollInfo.q_3)
async def question_three(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            "q_3": text
        }
    )

    await message.answer('Четвёртый вопрос\n\n'
                         'Занимаетесь ли вы спортом, если да то каким')

    await PollInfo.q_4.set()


@dp.message_handler(state=PollInfo.q_4)
async def question_four(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            "q_4": text
        }
    )

    await message.answer('Пятый вопрос вопрос\n\n'
                         'Сколько вам лет')

    await PollInfo.q_5.set()


@dp.message_handler(state=PollInfo.q_5)
async def question_two(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            "q_5": text
        }
    )

    data = await state.get_data()

    q_1 = data.get('q_1')
    q_2 = data.get('q_2')
    q_3 = data.get('q_3')
    q_4 = data.get('q_4')
    q_5 = data.get('q_5')

    await message.answer('Ваши ответы на тестирование:\n\n'
                         f'Первый вопрос: {q_1}\n'
                         f'Второй вопрос: {q_2}\n'
                         f'Третий вопрос: {q_3}\n'
                         f'Четвёртый вопрос: {q_4}\n'
                         f'Пятый вопрос: {q_5}')

    await state.reset_state(True)



