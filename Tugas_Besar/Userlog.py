import requests
import json
class Userlog:
    def __init__(self):
        self.__id=None
        self.__NomorTelepon = None
        self.__Nama = None
        self.__Email = None
        self.__JenisKelamin = None
        self.__KataSandi = None
        self.__Rolename = None
        self.__Alamat = None
        self.__url = "http://f0833068.xsph.ru/Hotel/userlog_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def NomorTelepon(self):
        return self.__NomorTelepon
        
    @NomorTelepon.setter
    def NomorTelepon(self, value):
        self.__NomorTelepon = value
    @property
    def Nama(self):
        return self.__Nama
        
    @Nama.setter
    def Nama(self, value):
        self.__Nama = value
    @property
    def Email(self):
        return self.__Email
        
    @Email.setter
    def Email(self, value):
        self.__Email = value
    @property
    def JenisKelamin(self):
        return self.__JenisKelamin
        
    @JenisKelamin.setter
    def JenisKelamin(self, value):
        self.__JenisKelamin = value
    @property
    def KataSandi(self):
        return self.__KataSandi
        
    @KataSandi.setter
    def KataSandi(self, value):
        self.__KataSandi = value
    @property
    def Rolename(self):
        return self.__Rolename
        
    @Rolename.setter
    def Rolename(self, value):
        self.__Rolename = value
    @property
    def Alamat(self):
        return self.__Alamat
        
    @Alamat.setter
    def Alamat(self, value):
        self.__Alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_NomorTelepon(self, NomorTelepon):
        url = self.__url+"?NomorTelepon="+NomorTelepon
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__NomorTelepon = item['NomorTelepon']
            self.__Nama = item['Nama']
            self.__Email = item['Email']
            self.__JenisKelamin = item['JenisKelamin']
            self.__KataSandi = item['KataSandi']
            self.__Rolename = item['Rolename']
            self.__Alamat = item['Alamat']
        return data
    def simpan(self):
        payload = {
            "NomorTelepon":self.__NomorTelepon,
            "Nama":self.__Nama,
            "Email":self.__Email,
            "JenisKelamin":self.__JenisKelamin,
            "KataSandi":self.__KataSandi,
            "Rolename":self.__Rolename,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_NomorTelepon(self, NomorTelepon):
        url = self.__url+"?NomorTelepon="+NomorTelepon
        payload = {
            "NomorTelepon":self.__NomorTelepon,
            "Nama":self.__Nama,
            "Email":self.__Email,
            "JenisKelamin":self.__JenisKelamin,
            "KataSandi":self.__KataSandi,
            "Rolename":self.__Rolename,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_NomorTelepon(self,NomorTelepon):
        url = self.__url+"?NomorTelepon="+NomorTelepon
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
