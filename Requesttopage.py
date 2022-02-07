import requests# Імпорт бібліотеки для зв'язку з сайтом

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}# Параметри для імітації дії людини

class RequestToSiteSend:

    def __init__(self):
        self.request = requests# Ініціалізація бібліотеки requests

    def get_request_to_website(self, streetname):
        result = self.request.get("http://poltavaaircondition.online/get.php?streets={}".format(streetname),
                                  headers=headers)# Створення запиту на сайт PoltavaAirCondition.online
        data = result.text.split(":")# Обробка отриманих даних
        return data# Видача отриманих даних

def main(streetname):
    req = RequestToSiteSend()# Ініціалізація класу
    return req.get_request_to_website(streetname) # Виведення результату запиту

