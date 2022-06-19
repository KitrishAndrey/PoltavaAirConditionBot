import requests
import json

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}# Параметри для імітації дії людини

class RequestToDBSend:

    def __init__(self):
        self.request = requests# Ініціалізація бібліотеки requests

    def push_uid_streetid(self, uid, streetid):
        result = self.request.get("http://poltavaaircondition.online/bothourstate.php?pushuidstreetid={0}:{1}".format(uid, streetid),
                                  headers=headers)# Створення запиту на сайт PoltavaAirCondition.online
        answer = result.text# Обробка отриманих даних
        return answer# Видача отриманих даних

    def get_prime_streetid(self, uid):
        result = self.request.get("http://poltavaaircondition.online/bothourstate.php?getstreetid={}".format(uid),
                                  headers=headers)# Створення запиту на сайт PoltavaAirCondition.online
        streetid = result.text
        return streetid
    def get_data_for_charts_array(self, streetid):
        result = self.request.get(
            "http://poltavaaircondition.online/bothourstate.php?getdataforchartsarray={}".format(streetid),
            headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        return json.loads(result.text)

    def get_uid_streetid_state_array(self):
        result = self.request.get("http://poltavaaircondition.online/bothourstate.php?getuidstreetidstatearray={}".format(1),
                                  headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        return json.loads(result.text)

    def push_hour_state(self, uid, streetid, state):
        result = self.request.get(
            "http://poltavaaircondition.online/bothourstate.php?pushhourstate={0}:{1}:{2}".format(uid, streetid, state),
            headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        answer = result.text
        return answer

    def push_three_hour_state(self, uid, streetid, state):
        result = self.request.get(
            "http://poltavaaircondition.online/bothourstate.php?pushthreehourstate={0}:{1}:{2}".format(uid, streetid, state),
            headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        answer = result.text
        return answer

    def push_six_hour_state(self, uid, streetid, state):
        result = self.request.get(
            "http://poltavaaircondition.online/bothourstate.php?pushsixhourstate={0}:{1}:{2}".format(uid, streetid, state),
            headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        answer = result.text
        return answer

    def push_zero_state(self, uid):

        result = self.request.get(
            "http://poltavaaircondition.online/bothourstate.php?pushzerostate={0}".format(uid),
            headers=headers)  # Створення запиту на сайт PoltavaAirCondition.online
        answer = result.text
        return answer

def push_uid_streetid(uid, streetid):
    req = RequestToDBSend()# Ініціалізація класу
    return req.push_uid_streetid(uid, streetid) # Виведення результату запиту

def get_prime_streetid(uid):
    req = RequestToDBSend()# Ініціалізація класу
    return req.get_prime_streetid(uid) # Виведення результату запиту

def get_data_for_charts_array(streetid):
    req = RequestToDBSend()
    return req.get_data_for_charts_array(streetid)

def get_uid_streetid_state_array():
    req = RequestToDBSend()# Ініціалізація класу
    return req.get_uid_streetid_state_array() # Виведення результату запиту

def push_hour_state(uid, streetid, state):
    req = RequestToDBSend()# Ініціалізація класу
    return req.push_hour_state(uid, streetid, state) # Виведення результату запиту

def push_three_hour_state(uid, streetid, state):
    req = RequestToDBSend()# Ініціалізація класу
    return req.push_three_hour_state(uid, streetid, state) # Виведення результату запиту

def push_six_hour_state(uid, streetid, state):
    req = RequestToDBSend()# Ініціалізація класу
    return req.push_six_hour_state(uid, streetid, state) # Виведення результату запиту

def push_zero_state(uid):
    req = RequestToDBSend()# Ініціалізація класу
    return req.push_zero_state(uid) # Виведення результату запиту
