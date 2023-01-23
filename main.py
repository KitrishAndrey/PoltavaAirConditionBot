import asyncio
import DBRequest
import Requesttopage
import StreetMessageText
from aiogram.utils.exceptions import BotBlocked
from aiogram import Bot, Dispatcher, executor, types

# Bot api_token
TOKEN = "-----"

#Delay

DELAY = 10

# Marcaps
markupmainmenu = types.InlineKeyboardMarkup(row_width=100)
streets = types.InlineKeyboardMarkup(row_width=100)
markupdetails = types.InlineKeyboardMarkup(row_width=100)
author = types.InlineKeyboardMarkup(row_width=100)
primemenu = types.InlineKeyboardMarkup(row_width=100)
onofmenu = types.InlineKeyboardMarkup(row_width=100)

# Main menu
menuitem = types.InlineKeyboardButton("Якість повітря🌫", callback_data="sensors")
pushkinastreet = types.InlineKeyboardButton("вул. Пушкіна", callback_data="pushkinska")
petryurstreet = types.InlineKeyboardButton("вул. Петра Юрченка", callback_data="petryur")
shevstreet = types.InlineKeyboardButton("вул. Шевченка", callback_data="shevchenka")
gromadstreet = types.InlineKeyboardButton("вул. Громадська", callback_data="gromad")
shkilnystreet = types.InlineKeyboardButton("Шкільний провулок", callback_data="shkilny")
velykotyrstreet = types.InlineKeyboardButton("вул. Великотирнівська", callback_data="velykotyr")
hoursdata = types.InlineKeyboardButton("⏰Повідомляти що години", callback_data="hourdata")
towebsite = types.InlineKeyboardButton("🚀Перейти на сайт", callback_data="towebsite",
                                       url='https://poltavaaircondition.online/polution/polutionmap.html')
primedata = types.InlineKeyboardButton("🧩Первинні дані", callback_data="primedata")
ruditimejun = types.InlineKeyboardButton("🎨Перейти на сторінку дизайнера🎨", callback_data= "ruditime",
                                         url="https://instagram.com/ruditime.junior?utm_medium=copy_link")
streetsprime = types.InlineKeyboardButton("🏘Інші датчики у місті Полтава", callback_data="sensors")
indexprime = types.InlineKeyboardButton("🔎Індекс якості повітря", callback_data="street")

removesignal = types.InlineKeyboardButton("❌🚫 Вимкнути оповіщення 🚫❌", callback_data="removesignal")

#User markups
markupmainmenu.add(menuitem)
streets.add(pushkinastreet).add(petryurstreet).add(shevstreet).add(gromadstreet).add(shkilnystreet).add(velykotyrstreet)
markupdetails.add(hoursdata, towebsite).add(primedata)
author.add(ruditimejun)
primemenu.add(streetsprime).add(towebsite).add(indexprime)

onofmenu.add(removesignal)

# Initialize bot and dispetcher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
DB = DBRequest

# starting bot

async def hourdatarequesting():
        while True:
            try:
                fr = DB.get_uid_streetid_state_array()
                for p in fr:
                    if "{0}".format(p.split(":")[2]) == "1":
                        await sendhourdata(p.split(":")[0], p.split(":")[1])
                await asyncio.sleep(3600)
            except BotBlocked:
                pass

async def sendhourdata(uid, streetid):
    if streetid == "shkilny":
        DB.push_uid_streetid(uid, "shkilny")
        message_text = Requesttopage.main("shkilny")
        street = "Шкільний провулок"
        AQI = float(message_text[0])
        message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
        if AQI <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 51 and AQI <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 101 and AQI <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 151 and AQI <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 201 and AQI <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "pushki":
        DB.push_uid_streetid(uid, "pushki")
        message_text = Requesttopage.main("pushkinska")
        street = "вул. Пушкіна"
        AQIPUSH = float(message_text[0])
        message_to_user = StreetMessageText.main(AQIPUSH, float(message_text[1]), street)
        if AQIPUSH <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQIPUSH >= 51 and AQIPUSH <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQIPUSH >= 101 and AQIPUSH <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQIPUSH >= 151 and AQIPUSH <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQIPUSH >= 201 and AQIPUSH <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "petryu":
        DB.push_uid_streetid(uid, "petryu")
        message_text = Requesttopage.main("petryur")
        street = "вул. Петра Юрченка"
        AQI = float(message_text[0])
        message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
        if AQI <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 51 and AQI <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 101 and AQI <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 151 and AQI <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 201 and AQI <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "shevch":
        DB.push_uid_streetid(uid, "shevch")
        message_text = Requesttopage.main("shevchenka")
        street = "вул. Шевченка"
        AQI = float(message_text[0])
        message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
        if AQI <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 51 and AQI <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 101 and AQI <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 151 and AQI <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 201 and AQI <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "gromad":
        DB.push_uid_streetid(uid, "gromad")
        message_text = Requesttopage.main("gromad")
        street = "вул. Громадська"
        AQI = float(message_text[0])
        message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
        if AQI <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 51 and AQI <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 101 and AQI <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 151 and AQI <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 201 and AQI <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "velyko":
        DB.push_uid_streetid(uid, "velyko")
        message_text = Requesttopage.main("velykotyr")
        street = "вул. Великотирнівська"
        AQI = float(message_text[0])
        message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
        if AQI <= 50:
            imgok = open("OKEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 51 and AQI <= 100:
            imgok = open("EVERLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 101 and AQI <= 150:
            imgok = open("ORANGELEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 151 and AQI <= 200:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)
        elif AQI >= 201 and AQI <= 1000:
            imgok = open("PERPELLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_message(message.chat.id, "    🙂️Вітаємо Вас, {}🙂️\n ♻️Ви користуєтесь еко-ботом міста Полтава♻️\n "
                                            "Для перегляду стану повітря, \n натисність на кнопку «Якість повітря», або "
                                            "введіть коману /airquality ."
                           .format(
                message.from_user.first_name),
                           parse_mode="html", reply_markup=markupmainmenu)

@dp.message_handler(commands=["airquality"])
async def start(message: types.Message):
    img = open("map.png", 'rb')
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(message.chat.id, img, "🏘🚩Оберіть вулицю на якій розташовано бажаний датчик🚩\n",
                         reply_markup=streets)

# help message
@dp.message_handler(commands=["about"])
async def help(message: types.Message):
    stiker = open("PoltavaAirConditionSticker.webp", "rb")
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_sticker(message.chat.id, stiker)
    await bot.send_message(message.chat.id, "   ⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️\n"
                                            "\n♻    Можливості PoltavaAirConditionbot    ♻\n"
                                            "\n▪Обравши «Якість повітря» Ви потрапите у меню вибору станції моніторингу якості повітря,\n"
                                            "де вам потрібно обрати бажаний датчик✅\n"
                                            "\n▪Також Ви можете увімкнути регулярне повідомлення про стан повітря на обраній вулиці 🏘 \n"
                                            "\n__________♻️❇Фірмові стікери️❇♻__________\n"
                                            "\nhttps://t.me/addstickers/cloudit\n"
                                            "\n▪Автор та дизайнер стікерів - @ruditimejunior\n"
                                            "\n⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️\n", reply_markup=author)

# inline menu, parsing and other

@dp.callback_query_handler(lambda c: c.data == "ruditime")
async def ruditime(call: types.CallbackQuery):
    return 0

@dp.callback_query_handler(lambda c: c.data == "sensors")
async def call_back_street(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    img = open("map.png", 'rb')
    await bot.send_chat_action(call.from_user.id, "typing")
    await bot.send_photo(call.from_user.id, img, "🏘🚩Оберіть вулицю на якій розташовано бажаний датчик🚩🏘\n",
                           reply_markup=streets)

@dp.callback_query_handler(lambda c: c.data == "towebsite")
async def call_back_air():
    return 0

@dp.callback_query_handler(lambda c: c.data == "primedata")
async def call_back_primedata(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    state = DB.get_prime_streetid(call.from_user.id)
    if state == "shkilny":
        street = "Шкліьний провулок"
        streetid = "shkilny"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)
    elif state == "pushki":
        street = "вул. Пушкіна"
        streetid = "pushkinska"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)
    elif state == "petryu":
        street = "вул. Петра Юрченка"
        streetid = "petryur"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)
    elif state == "shevch":
        street = "вул. Шевченка"
        streetid = "shevchenka"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)
    elif state == "gromad":
        street = "вул. Громадська"
        streetid = "gromad"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)
    elif state == "velyko":
        street = "вул. Великотирнівська"
        streetid = "velykotyr"
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, StreetMessageText.primedata(street, streetid), reply_markup=primemenu)

@dp.callback_query_handler(lambda c: c.data == "street")
async def call_back_primedata(call: types.CallbackQuery):
    state = DB.get_prime_streetid(call.from_user.id)
    await bot.send_chat_action(call.from_user.id, "typing")
    if state == "shkilny":
        await call_back_streetshkil(call)
    elif state == "pushki":
        await call_back_streetspushkin(call)
    elif state == "petryu":
        await call_back_streetpetr(call)
    elif state == "shevch":
        await call_back_streetshevchenka(call)
    elif state == "gromad":
        await call_back_streetsgromad(call)
    elif state == "velyko":
        await call_back_streetsvelykotyr(call)

@dp.callback_query_handler(lambda c: c.data == "hourdata")
async def call_back_hourdata(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    state = DB.get_prime_streetid(call.from_user.id)
    if state == "shkilny":
        streetid = "shkilny"
        DB.push_hour_state(call.from_user.id, streetid, 1)
    elif state == "pushki":
        streetid = "pushki"
        await bot.answer_callback_query(call.id)
        DB.push_hour_state(call.from_user.id, streetid, 1)
    elif state == "petryu":
        streetid = "petryu"
        await bot.answer_callback_query(call.id)
        DB.push_hour_state(call.from_user.id, streetid, 1)
    elif state == "shevch":
        streetid = "shevch"
        await bot.answer_callback_query(call.id)
        DB.push_hour_state(call.from_user.id, streetid, 1)
    elif state == "gromad":
        streetid = "gromad"
        await bot.answer_callback_query(call.id)
        DB.push_hour_state(call.from_user.id, streetid, 1)
    elif state == "velyko":
        streetid = "velyko"
        await bot.answer_callback_query(call.id)
        DB.push_hour_state(call.from_user.id, streetid, 1)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "🖥⏰📡Що годинне оповіщення увімкнуте📡⏰🖥", reply_markup=onofmenu)

@dp.callback_query_handler(lambda c: c.data == "removesignal")
async def call_back_remove_signals(call: types.CallbackQuery):
    DB.push_zero_state(call.from_user.id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "🖥⏰📡Що годинне оповіщення вимкнуте📡⏰🖥")

@dp.callback_query_handler(lambda c: c.data =="shkilny")
async def call_back_streetshkil(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "shkilny")
    message_text = Requesttopage.main("shkilny")
    street = "Шкільний провулок"
    AQI = float(message_text[0])
    message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
    if AQI <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 51 and AQI <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 101 and AQI <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 151 and AQI <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 201 and AQI <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="pushkinska")
async def call_back_streetspushkin(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "pushki")
    message_text = Requesttopage.main("pushkinska")
    street = "вул. Пушкіна"
    AQIPUSH = float(message_text[0])
    message_to_user = StreetMessageText.main(AQIPUSH, float(message_text[1]), street)
    if AQIPUSH <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQIPUSH >= 51 and AQIPUSH <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQIPUSH >= 101 and AQIPUSH <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQIPUSH >= 151 and AQIPUSH <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQIPUSH >= 201 and AQIPUSH <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="petryur")
async def call_back_streetpetr(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "petryu")
    message_text = Requesttopage.main("petryur")
    street = "вул. Петра Юрченка"
    AQI = float(message_text[0])
    message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
    if AQI <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 51 and AQI <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 101 and AQI <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 151 and AQI <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 201 and AQI <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="shevchenka")
async def call_back_streetshevchenka(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "shevch")
    message_text = Requesttopage.main("shevchenka")
    street = "вул. Шевченка"
    AQI = float(message_text[0])
    message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
    if AQI <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 51 and AQI <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 101 and AQI <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 151 and AQI <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 201 and AQI <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="gromad")
async def call_back_streetsgromad(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "gromad")
    message_text = Requesttopage.main("gromad")
    street = "вул. Громадська"
    AQI = float(message_text[0])
    message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
    if AQI <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 51 and AQI <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 101 and AQI <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 151 and AQI <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 201 and AQI <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="velykotyr")
async def call_back_streetsvelykotyr(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    DB.push_uid_streetid(call.from_user.id, "velyko")
    message_text = Requesttopage.main("velykotyr")
    street = "вул. Великотирнівська"
    AQI = float(message_text[0])
    message_to_user = StreetMessageText.main(float(message_text[0]), float(message_text[1]), street)
    if AQI <=50 :
        imgok = open("OKEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 51 and AQI <=100:
        imgok = open("EVERLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 101 and AQI <= 150:
        imgok = open("ORANGELEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 151 and AQI <= 200:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)
    elif AQI >= 201 and AQI <= 1000:
        imgok = open("PERPELLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.message_handler(content_types=["text"])
async def la_la_la(message):

    if message.chat.type == "private":
        if message.text:
            await bot.send_chat_action(message.chat.id, "typing")
            await bot.send_message(message.chat.id, "Нажаль, бот не сприймає такий вид повідомлень📥😕\n"
                                                    "Будь ласка, використовуйте меню та відповідні кнопки📲🙂")

@dp.message_handler(content_types=["voice"])
async def la_la_la(message):

    if message.chat.type == "private":
        if message.voice:
            await bot.send_chat_action(message.chat.id, "typing")
            await bot.send_message(message.chat.id, "Нажаль, бот не сприймає такий вид повідомлень📥😕\n"
                                                    "Будь ласка, використовуйте меню та відповідні кнопки📲🙂")

async def on_startup(x):
  asyncio.create_task(hourdatarequesting())

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
