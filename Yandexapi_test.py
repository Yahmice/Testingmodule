import requests
from token_ya import TOKEN_ #Личный токен

def folder_creation():
    url = f'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {TOKEN_}'}
    params = {'path': f'Photos',
              'overwrite': 'false'}
    response = requests.put(url=url, headers=headers, params=params)
    return f'papka sozdana'

def folder_creation_status():
    url = f'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {TOKEN_}'}
    params = {'path': f'Photos',
              'overwrite': 'false'}
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code
