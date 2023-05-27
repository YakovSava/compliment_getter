from json import loads
from downoloader import Load

load = Load()

def get_compliment() -> str:
    with open('compliments.json', 'r', encoding='utf-8') as file:
        compliemnts = loads(file.read())['compliments']
    return load.choice(compliemnts)

for _ in range(5):
    print(get_compliment())