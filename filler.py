import translators as ts

from time import sleep
from json import loads, dumps
from requests import session, Session

def _load_json() -> dict:
    with open('compliments.json', 'r', encoding='utf-8') as file:
        return loads(file.read())

def _save_json(data:dict={'compliments': []}) -> None:
    with open('compliments.json', 'w', encoding='utf-8') as file:
        file.write(dumps(data))\

def _get_compliment(sess:Session) -> str:
    resp = sess.get('https://8768zwfurd.execute-api.us-east-1.amazonaws.com/v1/compliments').text
    raw = ts.translate_text(resp[1:-1], to_language='ru')
    decoded = raw.encode().decode('unicode_escape')
    return ''.join(chr(int(x, 16)) for x in decoded.split('\\u')[1:])

def main():
    data = _load_json()
    with session() as sess:
        data['compliments'].extend([_get_compliment(sess) for _ in range(1000)])
        sleep(5)
    _save_json(data=data)

if __name__ == '__main__':
    main()