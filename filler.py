from json import loads, dumps
from requests import session

def _load_json():
    with open('compliments.json', 'r', encoding='utf-8') as file:
        return loads(file.read())

def _save_json(data:dict={'compliments': []}):
    with open('compliments.json', 'w', encoding='utf-8') as file:
        file.write(dumps(data))