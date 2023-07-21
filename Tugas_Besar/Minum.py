import requests
import json
class Minum:
    def __init__(self):
        self.__id=None
        self.__IDMinuman = None
        self.__NamaMinuman = None
        self.__Harga = None
        self.__url = "http://f0833068.xsph.ru/Hotel/minum_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def IDMinuman(self):
        return self.__IDMinuman
        
    @IDMinuman.setter
    def IDMinuman(self, value):
        self.__IDMinuman = value
    @property
    def NamaMinuman(self):
        return self.__NamaMinuman
        
    @NamaMinuman.setter
    def NamaMinuman(self, value):
        self.__NamaMinuman = value
    @property
    def Harga(self):
        return self.__Harga
        
    @Harga.setter
    def Harga(self, value):
        self.__Harga = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_IDMinuman(self, IDMinuman):
        url = self.__url+"?IDMinuman="+IDMinuman
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__IDMinuman = item['IDMinuman']
            self.__NamaMinuman = item['NamaMinuman']
            self.__Harga = item['Harga']
        return data
    def simpan(self):
        payload = {
            "IDMinuman":self.__IDMinuman,
            "NamaMinuman":self.__NamaMinuman,
            "Harga":self.__Harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_IDMinuman(self, IDMinuman):
        url = self.__url+"?IDMinuman="+IDMinuman
        payload = {
            "IDMinuman":self.__IDMinuman,
            "NamaMinuman":self.__NamaMinuman,
            "Harga":self.__Harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_IDMinuman(self,IDMinuman):
        url = self.__url+"?IDMinuman="+IDMinuman
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
