import io
import asyncio
import Requesttopage
import StreetMessageText
from aiogram import Bot, Dispatcher, executor, types

# Bot api_token
TOKEN = "5069999254:AAF4IZZu3sK-0qTotl98dkV-SrcHFLF_rx8"

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

# starting bot

def ustreet(uid, streetid):
    try:
        with open("utreetid.txt", "r") as file:
            f =file.readlines()
        with open("utreetid.txt", "r") as file:
            if f[len(f) - 1] == str("\n"):
                f.remove(str("\n"))
                n = file.read()
                n = n.replace("{0}".format(n), '{0}'.format(''.join(f)))
                file.write(n)

        with open("utreetid.txt", "r+") as file:
            fel = file.readlines()
            arrid = [int(i.split(":")[0]) for i in fel]
            if int(uid) not in arrid:
                file.writelines("{0}:{1}\n".format(uid, streetid))

        with open("utreetid.txt", "r") as file:
            x = file.read()
        with open("utreetid.txt", "r+") as file:
            for i in fel:
                if i.startswith(str(uid)):
                    x = x.replace("{0}".format(i), "{0}:{1}\n".format(uid, streetid))
                    file.write(x)
                else:
                    return 0
    except Exception as e:
        print(repr(e))

def getuserprimestreet(uid):
    with open("utreetid.txt", "r+") as file:
        fel = file.readlines()
        for i in fel:
            if i.startswith(str(uid)):
                return str(i.split(":")[1][:-1])

def writestate(uid, streetid, state):
    try:
        with open("uid.txt", "r+") as f:
            fr = f.readlines()
            for i in fr:
                arrid = [i.split(":")[0]]
            if str(uid) not in arrid:
                f.writelines("{0}:{1}:{2}\n".format(uid, streetid, state))
                f.close()

        with open("uid.txt", "r") as file:
            x = file.read()
        with io.open("uid.txt", "r+") as file:
            for i in fr:
                if i.startswith(str(uid)):
                    x = x.replace("{0}".format(i), "{0}:{1}:{2}\n".format(uid, streetid, state))
                    file.write(x)
                else:
                    return 0
    except Exception as e:
        print(repr(e))

async def changestate(uid):
    try:
        with open("uid.txt", "r+") as f:
            fr = f.readlines()
        with open("uid.txt", "r") as file:
            x = file.read()
        with io.open("uid.txt", "r+") as file:
            for i in fr:
                if i.startswith(str(uid)):
                    x = x.replace("{0}".format(i), "{0}:{1}:{2}".format(i.split(":")[0], i.split(":")[1], 0))
                    file.write(x)
                else:
                    return 0
    except Exception as e:
        print(repr(e))

async def hourdatarequesting():
    while True:
        with open("uid.txt", "r+") as f:
            fr = f.readlines()
            for i in fr:
                if i.split(":")[2][:-1] == str(1):
                    await sendhourdata(i.split(":")[0], i.split(":")[1])
                    await asyncio.sleep(3600)
                else:
                    await asyncio.sleep(3600)
                    return 1

async def sendhourdata(uid, streetid):
    if streetid == "shkilny":
        ustreet(uid, "shkilny")
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
        elif AQI >= 200 and AQI <= 300:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "pushki":
        ustreet(uid, "pushki")
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
        elif AQIPUSH >= 200 and AQIPUSH <= 300:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)


    elif streetid == "petryu":
        ustreet(uid, "petryu")
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
        elif AQI >= 200 and AQI <= 300:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "shevch":
        ustreet(uid, "shevch")
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
        elif AQI >= 200 and AQI <= 300:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "gromad":
        ustreet(uid, "gromad")
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
        elif AQI >= 200 and AQI <= 300:
            imgok = open("REDLEVEL.png", "rb")
            await bot.send_photo(uid, imgok, message_to_user, reply_markup=markupdetails)

    elif streetid == "velyko":
        ustreet(uid, "velyko")
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
        elif AQI >= 200 and AQI <= 300:
            imgok = open("REDLEVEL.png", "rb")
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
                                            "\n▪Еко-ботом можна керувати за допомогою голосових повідомлень 🗣\n"
                                            "\n▪Просто скажіть боту напис на кнопці на яку хотіли б «натиснути»\n"
                                            "\n__________♻️❇Фірмові стікери️❇♻__________\n"
                                            "\nhttps://t.me/addstickers/cloudit\n"
                                            "\n▪Автор та дизайнер - @ruditimejunior\n"
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
    state = getuserprimestreet(call.from_user.id)
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
    state = getuserprimestreet(call.from_user.id)
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
    state = getuserprimestreet(call.from_user.id)
    if state == "shkilny":
        streetid = "shkilny"
        writestate(call.from_user.id, streetid, 1)
    elif state == "pushki":
        streetid = "pushki"
        await bot.answer_callback_query(call.id)
        writestate(call.from_user.id, streetid, 1)
    elif state == "petryu":
        streetid = "petryu"
        await bot.answer_callback_query(call.id)
        writestate(call.from_user.id, streetid, 1)
    elif state == "shevch":
        streetid = "shevch"
        await bot.answer_callback_query(call.id)
        writestate(call.from_user.id, streetid, 1)
    elif state == "gromad":
        streetid = "gromad"
        await bot.answer_callback_query(call.id)
        writestate(call.from_user.id, streetid, 1)
    elif state == "velyko":
        streetid = "velyko"
        await bot.answer_callback_query(call.id)
        writestate(call.from_user.id, streetid, 1)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "🖥⏰📡Що годинне оповіщення увімкнуте📡⏰🖥", reply_markup=onofmenu)

@dp.callback_query_handler(lambda c: c.data == "removesignal")
async def call_back_remove_signals(call: types.CallbackQuery):
    await changestate(call.from_user.id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "🖥⏰📡Що годинне оповіщення вимкнуте📡⏰🖥")

@dp.callback_query_handler(lambda c: c.data =="shkilny")
async def call_back_streetshkil(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "shkilny")
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
    elif AQI >= 200 and AQI <= 300:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="pushkinska")
async def call_back_streetspushkin(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "pushki")
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
    elif AQIPUSH >= 200 and AQIPUSH <= 300:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="petryur")
async def call_back_streetpetr(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "petryu")
    message_text = Requesttopage.main("petryur")
    street = "вул. Петра Юрченка"
    AQI = float(message_text[0])
    print(AQI)
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
    elif AQI >= 200 and AQI <= 300:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)


@dp.callback_query_handler(lambda c: c.data =="shevchenka")
async def call_back_streetshevchenka(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "shevch")
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
    elif AQI >= 200 and AQI <= 300:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="gromad")
async def call_back_streetsgromad(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "gromad")
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
    elif AQI >= 200 and AQI <= 300:
        imgok = open("REDLEVEL.png", "rb")
        await bot.answer_callback_query(call.id)
        await bot.send_photo(call.from_user.id, imgok, message_to_user, reply_markup=markupdetails)

@dp.callback_query_handler(lambda c: c.data =="velykotyr")
async def call_back_streetsvelykotyr(call: types.CallbackQuery):
    await bot.send_chat_action(call.from_user.id, "typing")
    ustreet(call.from_user.id, "velyko")
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
    elif AQI >= 200 and AQI <= 300:
        imgok = open("REDLEVEL.png", "rb")
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
