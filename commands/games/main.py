import random
from aiogram import types, Dispatcher
from commands.db import url_name, get_balance, getstatus
from commands.main import win_luser
from commands.games.db import *


def get_summ(msg, balance):
    if msg.text.lower().split()[1] in ['все', 'всё']:
        return balance

    summ = msg.text.split()[1].replace('е', 'e')
    return int(float(summ))


async def darts_cmd(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    balance = await get_balance(user_id)
    url = await url_name(user_id)

    try:
        summ = get_summ(message, balance)
    except:
        await message.answer(f'{url}, вы не ввели ставку для игры {rloser}')
        return

    if balance >= summ:
        if summ >= 10:
            gt = await gametime(user_id)
            if gt == 1:
                await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
                return

            rx1 = await message.reply_dice(emoji="🎯")
            rx = rx1.dice.value

            if int(rx) == 5:
                await message.answer(f'{url}, вы были на волоске от победы! 🎯\n💰 Ваши средства в безопасности! (х1)')

            elif int(rx) == 6:
                c = Decimal(summ * 2)
                c2 = round(c)
                c2 = '{:,}'.format(c2).replace(',', '.')
                await gXX(user_id, c, 1)
                await message.answer(f'{url}, в яблочко! 🎯\n💰 Ваш приз: {c2}$!')

            else:
                await gXX(user_id, summ, 0)
                await message.answer(f'{rloser} | К сожалению Ваша победа ускользнула от Вас! 🎯️')

        else:
            await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')
    else:
        await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса {rloser}')


async def kybik_game_cmd(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    try:
        ch = int(message.text.split()[1])

        if message.text.lower().split()[2] in ['все', 'всё']:
            summ = balance
        else:
            summ = message.text.split()[2].replace('е', 'e')
            summ = int(float(summ))
    except:
        await message.answer(f'{rloser} | Ошибка. Вы не ввели ставку для игры.')
        return

    if ch in range(1, 7):
        if balance >= summ:
            if summ >= 10:
                gt = await gametime(user_id)
                if gt == 1:
                    await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
                    return

                rx1 = await message.reply_dice(emoji="🎲")
                rx = rx1.dice.value

                if int(rx) == ch:
                    c = Decimal(summ * 4)
                    c2 = round(c)
                    c2 = '{:,}'.format(c2).replace(',', '.')
                    await gXX(user_id, c, 1)
                    await message.answer(f'{rwin} | Поздравляю! Вы угадали число. Ваш выигрыш составил - {c2}$')
                    return
                else:
                    await gXX(user_id, summ, 0)
                    await message.answer(f'{rwin} | К сожалению вы не угадали число! 🎲')
                    return

            else:
                await message.answer(f'{rloser} | Ваша ставка не может быть меньше 10.')
        else:
            await message.answer(f'{rloser} | Недостаточно средств.')
    else:
        t = 'меньше 0' if ch < 1 else 'больше 6'
        await message.answer(f'{rloser} | Ошибка. Вы не можете поставить на число {t}.')


async def basketbol_cmd(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    try:
        summ = get_summ(message, balance)
    except:
        await message.reply(f'{url}, вы не ввели ставку для игры 😞')
        return

    if balance < summ:
        await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса 😕')
        return

    gt = await gametime(user_id)
    if gt == 1:
        await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
        return

    if summ >= 10:
        rx1 = await message.reply_dice(emoji="🏀")
        rx = rx1.dice.value

        if int(rx) == 5:
            c = Decimal(summ * 2)
            c2 = round(c)
            c2 = '{:,}'.format(c2).replace(',', '.')
            await gXX(user_id, c, 1)
            await message.answer(f'{url}, мяч в кольце, ура! 🏀\n💰 Ваш приз: {c2}$!')

        elif int(rx) == 4:
            await message.answer(f'{url}, бросок оказался на грани фола! 🏀\n💰 Ваши средства в безопасности! (х1)')
        else:
            await gXX(user_id, summ, 0)
            await message.answer(f'{rwin} | К сожалению вы не попали в кольцо! 🏀')
    else:
        await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')


async def bowling_cmd(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    try:
        summ = get_summ(message, balance)
    except:
        await message.reply(f'{url}, вы не ввели ставку для игры 😞')
        return

    if balance < summ:
        await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса 😕')
        return

    gt = await gametime(user_id)
    if gt == 1:
        await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
        return

    if summ >= 10:
        rx1 = await message.reply_dice(emoji="🎳️")
        rx = rx1.dice.value

        if int(rx) == 6:
            c = Decimal(summ * 2)
            c2 = round(c)
            c2 = '{:,}'.format(c2).replace(',', '.')
            await gXX(user_id, c, 1)
            await message.answer(f'{url}, страйк! Полная победа! 🎳️\n💰 Ваш приз: {c2}$!')

        elif int(rx) == 5:
            await message.answer(f'{url}, так близко к победе! 🎳\n💰 Ваши средства в безопасности! (х1)')
        else:
            await gXX(user_id, summ, 0)
            await message.answer(f'{rwin} | К сожалению мимо всех кеглей! 🎳')
    else:
        await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')


async def game_casino(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    coff_dict = {
        0: [2, 1.75, 1.5, 1.25, 0.75, 0.5, 0.25, 0.1],
        1: [2, 1.75, 1.5, 1.25, 0.75, 0.5, 0.25],
        4: [2.25, 1.75, 1.5, 1.25, 0.75, 0.5, 0.25],
    }

    try:
        summ = get_summ(message, balance)
    except:
        return await message.answer(f'{url}, вы не ввели ставку для игры {rloser}')

    if balance < summ:
        return await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса {rloser}')

    gt = await gametime(user_id)
    if gt == 1:
        await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
        return

    if summ >= 10:
        status = await getstatus(user_id)
        coff = coff_dict.get(status, coff_dict[1])
        x = random.choice(coff)

        if x > 1:
            c = int(summ * x - summ)
            txt = f'{url}, вы выиграли <summ>$ (x{x})  {rwin}'
            await gXX(user_id, c, 1)
        else:
            c = summ - int(summ * x)
            txt = f'{url}, вы проиграли <summ>$ (x{x})  {rloser}'
            await gXX(user_id, c, 0)

        c2 = '{:,}'.format(c).replace(',', '.')
        await message.answer(txt.replace('<summ>', c2))

    else:
        await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')


async def game_spin(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    emojis = ['🎰', '🍓', '🍒', '💎', '🍋', '🌕', '🖕', '💰', '🍎', '🎁', '💎', '💩', '🍩', '🍗', '🍏', '🔥', '🍊']

    try:
        summ = get_summ(message, balance)
    except:
        return await message.answer(f'{url}, вы не ввели ставку для игры {rloser}')

    if balance < summ:
        return await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса {rloser}')

    gt = await gametime(user_id)
    if gt == 1:
        await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
        return

    if summ >= 10:
        emojis = [random.choice(emojis) for _ in range(3)]
        emj = '|{}|{}|{}|'.format(*emojis)

        payout = 0
        unique_emojis = set(emojis)
        for emoji in unique_emojis:
            if emoji == '💎' or emoji == '🍋':
                payout += summ * 0.25
            elif emoji == '🎰':
                payout += summ
        if len(unique_emojis) == 1:
            payout += summ * 5

        if payout != 0:
            c2 = '{:,}'.format(int(summ + payout)).replace(',', '.')
            await gXX(user_id, payout, 1)
            await message.answer(f'{url}\n{emj} выигрыш: {c2}$')
        else:
            await message.answer(f'{url}\n{emj} Удача не на твоей стороне. Выигрыш: 0$')
            await gXX(user_id, summ, 0)
    else:
        await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')


async def game_trade(message: types.Message):
    user_id = message.from_user.id
    rwin, rloser = await win_luser()
    url = await url_name(user_id)
    balance = await get_balance(user_id)

    try:
        action = message.text.split()[1]

        if message.text.lower().split()[2] in ['все', 'всё']:
            summ = balance
        else:
            summ = message.text.split()[2].replace('е', 'e')
            summ = int(float(summ))
    except:
        return await message.answer(f'{url}, вы не ввели ставку для игры {rloser}')

    if action.lower() not in ['вверх', 'вниз']:
        return

    if balance < summ:
        return await message.answer(f'{url}, ваша ставка не может быть больше вашего баланса {rloser}')

    gt = await gametime(user_id)
    if gt == 1:
        await message.answer(f'{url}, играть можно каждые 5 секунд. Подождите немного {rloser}')
        return

    if summ >= 10:
        random_number = random.randint(0, 100)
        random_direction = random.randint(1, 2)

        if random_direction == 1:
            result = 'вверх' if action.lower() == 'вверх' else 'вниз'
        else:
            result = 'вниз' if action.lower() == 'вверх' else 'вверх'

        if action.lower() == result:
            payout = int(summ + (summ * random_number / 100))
            c2 = '{:,}'.format(payout).replace(',', '.')
            await message.answer(f'{url}\n📈 Курс пошёл {result} на {random_number}%\n✅ Ваш выигрыш составил - {c2}$')
            await gXX(user_id, payout, 1)
        else:
            payout = int(summ - (summ * random_number / 100))
            await message.answer(f'{url}\n📈 Курс пошёл {result} на {random_number}%\n❌ Ваш выигрыш составил - 0$')
            await gXX(user_id, payout, 0)
    else:
        await message.answer(f'{url}, ваша ставка не может быть меньше 10 {rloser}')


def reg(dp: Dispatcher):
    dp.register_message_handler(darts_cmd, lambda message: message.text.lower().startswith('дартс'))
    dp.register_message_handler(kybik_game_cmd, lambda message: message.text.lower().startswith('кубик'))
    dp.register_message_handler(basketbol_cmd, lambda message: message.text.lower().startswith('баскетбол'))
    dp.register_message_handler(bowling_cmd, lambda message: message.text.lower().startswith('боулинг'))
    dp.register_message_handler(game_casino, lambda message: message.text.lower().startswith('казино'))
    dp.register_message_handler(game_spin, lambda message: message.text.lower().startswith('спин'))
    dp.register_message_handler(game_trade, lambda message: message.text.lower().startswith(("трейд вверх", "трейд вниз")))
