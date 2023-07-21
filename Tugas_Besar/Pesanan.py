import requests
import json
class Pesanan:
    def __init__(self):
        self.__id=None
        self.__NoPesanan = None
        self.__Pemesan = None
        self.__Barang = None
        self.__Kuantitas = None
        self.__TotalHarga = None
        self.__url = "http://f0833068.xsph.ru/Hotel/pesanan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def NoPesanan(self):
        return self.__NoPesanan
        
    @NoPesanan.setter
    def NoPesanan(self, value):
        self.__NoPesanan = value
    @property
    def Pemesan(self):
        return self.__Pemesan
        
    @Pemesan.setter
    def Pemesan(self, value):
        self.__Pemesan = value
    @property
    def Barang(self):
        return self.__Barang
        
    @Barang.setter
    def Barang(self, value):
        self.__Barang = value
    @property
    def Kuantitas(self):
        return self.__Kuantitas
        
    @Kuantitas.setter
    def Kuantitas(self, value):
        self.__Kuantitas = value
    @property
    def TotalHarga(self):
        return self.__TotalHarga
        
    @TotalHarga.setter
    def TotalHarga(self, value):
        self.__TotalHarga = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_NoPesanan(self, NoPesanan):
        url = self.__url+"?NoPesanan="+NoPesanan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__NoPesanan = item['NoPesanan']
            self.__Pemesan = item['Pemesan']
            self.__Barang = item['Barang']
            self.__Kuantitas = item['Kuantitas']
            self.__TotalHarga = item['TotalHarga']
        return data
    def simpan(self):
        payload = {
            "NoPesanan":self.__NoPesanan,
            "Pemesan":self.__Pemesan,
            "Barang":self.__Barang,
            "Kuantitas":self.__Kuantitas,
            "TotalHarga":self.__TotalHarga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_NoPesanan(self, NoPesanan):
        url = self.__url+"?NoPesanan="+NoPesanan
        payload = {
            "NoPesanan":self.__NoPesanan,
            "Pemesan":self.__Pemesan,
            "Barang":self.__Barang,
            "Kuantitas":self.__Kuantitas,
            "TotalHarga":self.__TotalHarga
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_NoPesanan(self,NoPesanan):
        url = self.__url+"?NoPesanan="+NoPesanan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
