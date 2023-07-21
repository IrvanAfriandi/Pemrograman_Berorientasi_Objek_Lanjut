import requests
import json
class Kamar:
    def __init__(self):
        self.__id=None
        self.__IDKamar = None
        self.__KelasKamar = None
        self.__HargaPerMalam = None
        self.__StatusKamar = None
        self.__Penyewa = None
        self.__CheckIN = None
        self.__url = "http://f0833068.xsph.ru/Hotel/kamar_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def IDKamar(self):
        return self.__IDKamar
        
    @IDKamar.setter
    def IDKamar(self, value):
        self.__IDKamar = value
    @property
    def KelasKamar(self):
        return self.__KelasKamar
        
    @KelasKamar.setter
    def KelasKamar(self, value):
        self.__KelasKamar = value
    @property
    def HargaPerMalam(self):
        return self.__HargaPerMalam
        
    @HargaPerMalam.setter
    def HargaPerMalam(self, value):
        self.__HargaPerMalam = value
    @property
    def StatusKamar(self):
        return self.__StatusKamar
        
    @StatusKamar.setter
    def StatusKamar(self, value):
        self.__StatusKamar = value
    @property
    def Penyewa(self):
        return self.__Penyewa
        
    @Penyewa.setter
    def Penyewa(self, value):
        self.__Penyewa = value
    @property
    def CheckIN(self):
        return self.__CheckIN
        
    @CheckIN.setter
    def CheckIN(self, value):
        self.__CheckIN = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_IDKamar(self, IDKamar):
        url = self.__url+"?IDKamar="+IDKamar
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__IDKamar = item['IDKamar']
            self.__KelasKamar = item['KelasKamar']
            self.__HargaPerMalam = item['HargaPerMalam']
            self.__StatusKamar = item['StatusKamar']
            self.__Penyewa = item['Penyewa']
            self.__CheckIN = item['CheckIN']
        return data
    def simpan(self):
        payload = {
            "IDKamar":self.__IDKamar,
            "KelasKamar":self.__KelasKamar,
            "HargaPerMalam":self.__HargaPerMalam,
            "StatusKamar":self.__StatusKamar,
            "Penyewa":self.__Penyewa,
            "CheckIN":self.__CheckIN
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_IDKamar(self, IDKamar):
        url = self.__url+"?IDKamar="+IDKamar
        payload = {
            "IDKamar":self.__IDKamar,
            "KelasKamar":self.__KelasKamar,
            "HargaPerMalam":self.__HargaPerMalam,
            "StatusKamar":self.__StatusKamar,
            "Penyewa":self.__Penyewa,
            "CheckIN":self.__CheckIN
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_IDKamar(self,IDKamar):
        url = self.__url+"?IDKamar="+IDKamar
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
