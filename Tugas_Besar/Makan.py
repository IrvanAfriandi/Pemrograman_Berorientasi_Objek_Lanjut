import requests
import json
class Makan:
    def __init__(self):
        self.__id=None
        self.__IDMakanan = None
        self.__NamaMakanan = None
        self.__Harga = None
        self.__url = "http://f0833068.xsph.ru/Hotel/makan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def IDMakanan(self):
        return self.__IDMakanan
        
    @IDMakanan.setter
    def IDMakanan(self, value):
        self.__IDMakanan = value
    @property
    def NamaMakanan(self):
        return self.__NamaMakanan
        
    @NamaMakanan.setter
    def NamaMakanan(self, value):
        self.__NamaMakanan = value
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
    def get_by_IDMakanan(self, IDMakanan):
        url = self.__url+"?IDMakanan="+IDMakanan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__IDMakanan = item['IDMakanan']
            self.__NamaMakanan = item['NamaMakanan']
            self.__Harga = item['Harga']
        return data
    def simpan(self):
        payload = {
            "IDMakanan":self.__IDMakanan,
            "NamaMakanan":self.__NamaMakanan,
            "Harga":self.__Harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_IDMakanan(self, IDMakanan):
        url = self.__url+"?IDMakanan="+IDMakanan
        payload = {
            "IDMakanan":self.__IDMakanan,
            "NamaMakanan":self.__NamaMakanan,
            "Harga":self.__Harga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_IDMakanan(self,IDMakanan):
        url = self.__url+"?IDMakanan="+IDMakanan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
