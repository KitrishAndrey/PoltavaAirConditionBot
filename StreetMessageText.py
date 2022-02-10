import requests# Імпорт бібліотекі для зв'язку з сайтом
import pytz
import datetime
tz = pytz.timezone('Europe/Kiev')
ct = datetime.datetime.now(tz=tz)

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}# Параметри для імітації дії людини

class   StreetMessageText():

    def __init__(self):# Функція ініціалізації змінних
        self.request = requests
        self.year = ct.strftime("%Y-%m-%d")
        self.time = ct.strftime("%H:%M")

    def streetmessagetext(self, AQI, CO2, street):# Функція виводу тексту про стан повітря та індекс AQI
        data = "\n🏙Стан повітря у місті Полтава на вулиці '{0}'\n" \
               "\n" \
               "\n☁PM2.5  ➡️ {1} AQI\n" \
               "\n🚙CO2     ➡️ {2} AQI\n" \
               "\n" \
               "\n🕙 Данні станом на: {3} , {4}\n" \
               "\n📡 Данні представлені: PoltavaAirCondition\n".format(street, AQI, CO2, self.year, self.time)
        return data# Виведення отриманого тексту

    def streetmessageprimedata(self, street, streetid):# Функція виводу тексту первинних даних
        request = self.request.get("http://poltavaaircondition.online/get.php?primedata={0}".format(streetid),
                                  headers=headers)
        AQI =request.text.split(":")[0]
        CO2 = request.text.split(":")[1]
        Temp = request.text.split(":")[2]
        Hum = request.text.split(":")[3]
        Pres = request.text.split(":")[4]
        primedata = "\n🏙Первинні дані на датчику вулиці '{0}', у місті Полтава:\n" \
                    "\n☁PM2.5: {1} мкг/м³\n" \
                    "\n🚙CO2: {2} мкг/м³\n" \
                    "\n🌡️Температура: {3}°C\n"\
                    "\n💧Вологість: {4}%\n "\
                    "\n🌀Aтмосферний тиск: {5}гПа\n"\
                    "\n"\
                    "\n🕙 Данні станом на: {6} , {7}\n"\
                    "\n📡 Данні представлені: PoltavaAirCondition\n".format(street, AQI, CO2, Temp, Hum, Pres, self.year,
                                                                            self.time)
        return primedata# Вивід фінкції

def main(AQI, CO2, street):
    result = StreetMessageText()# Ініціалізація класу
    return result.streetmessagetext(AQI, CO2, street)#Отримання тексту о стані повітря та індексі AQI

def primedata(street, streetid):
    res = StreetMessageText()# Ініціалізіція класу
    return res.streetmessageprimedata(street, streetid)# Отримання тексту з первиними даними
