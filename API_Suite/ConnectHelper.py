import requests
import json

class ConnectHelper:

    User = 'Paul'
    Password = '12345'
    Lastname = 'Sablin'
    Phone = '1234567'

    url = "http://127.0.0.1:6969"
    token_headers = {
               "Content-Type": "application/json",
               "Token": None
              }

    def __init__(self, url = url):
        self._path = url
        self._token_headers = ConnectHelper.token_headers

    def get_token(self, defaultuser = User, defaultpassword = Password):
        path = f"{self._path}/api/auth/token"
        response = requests.get(path, auth=(defaultuser, defaultpassword))
        self._token_headers["Token"] = response.json()["token"]
        return response

    def get_user(self, username = User):
        path = f"{self._path}/api/users/{username}"
        response = requests.get(path, headers=self._token_headers)
        return response

    def put_user(self, username=User, first_name=None, last_name=None, phone=None, pass_word=None, user_name=None):
        path = f"{self._path}/api/users/{username}"
        json={}

        if (first_name):
            json["firstname"] = first_name

        if (last_name):
            json["lastname"] = last_name

        if (phone):
            json["phone"] = phone

        if (pass_word):
            json["password"] = pass_word

        if (user_name):
            json["username"] = user_name

        response = requests.put(path, headers=self._token_headers, json=json)
        return response

    def get_users(self):
        path = f"{self._path}/api/users"
        response = requests.get(path, headers=self._token_headers)
        return response

    def post_users(self, first_name=User, last_name=Lastname, phone=Phone, pass_word=Password, user_name=None):
        path = f"{self._path}/api/users"
        json = {
               "firstname":first_name,
               "lastname":last_name,
               "phone":phone,
               "password":pass_word,
               "username":first_name
               }
        if (user_name):
            json["username"] = user_name
        response = requests.post(path, headers=self._token_headers, json=json)
        return response
