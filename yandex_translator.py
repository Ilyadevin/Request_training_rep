import requests
from config import config_file
texts = []
languages = ['de', 'es', 'fr']
text_files = ['directories/DE.txt', 'directories/ES.txt', 'directories/FR.txt']
for i in text_files:
    with open(i, 'r') as file:
        texts.append(file.read())

API_KEY = config_file() # API Key
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'ru-{to_lang}',
    }

    response = requests.get(URL, params=params)

    return ''.join(response.json()['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    for j in languages:
        for g in texts:
            print(translate_it(g, j))
