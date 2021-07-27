import requests
from pprint import pprint
TOKEN = 'AQAAAAAFo08JAADLW4k7LIJX4UU0jEyzpOV26Tk'

class YaUploader:

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'}

    def check_created_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params={'path': path})
        return response.status_code


    def create_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, headers = self.get_headers(), params= {'path' : path})
        return response.status_code

