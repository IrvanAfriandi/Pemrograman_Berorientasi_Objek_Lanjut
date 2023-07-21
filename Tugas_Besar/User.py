import requests
class User:
    def __init__(self):
        self.__id=None
        self.__UserID = None
        self.__Username = None
        self.__Passwrd = None
        self.__Rolename = None
        self.__url = "http://f0833068.xsph.ru/Hotel/user_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def UserID(self):
        return self.__UserID
        
    @UserID.setter
    def UserID(self, value):
        self.__UserID = value
    @property
    def Username(self):
        return self.__Username
        
    @Username.setter
    def Username(self, value):
        self.__Username = value
    @property
    def Passwrd(self):
        return self.__Passwrd
        
    @Passwrd.setter
    def Passwrd(self, value):
        self.__Passwrd = value
    @property
    def Rolename(self):
        return self.__Rolename
    
    def Login(self):
        payload = {
            "Nama":self.__Username,
            "KataSandi":self.__Passwrd
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text