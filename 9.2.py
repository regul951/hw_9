import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        url = 'https://cloud-api.yandex.net:443/v1/disk'
        headers = {
            'Authorization': self.token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
                  }

        # Загрузка файла на диск
        # Получение ссылки на загрузку
        r = requests.get(url + '/resources/upload', headers=headers, params={'path': file_name})
        # Отправка файла
        requests.put(r.json()['href'], headers=headers, files={'f': open(file_path + file_name, 'rb')})
        return print(f'Загрузка {file_name} прошла успешно.')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь: ')
    name_of_file = input('Введите имя файла: ')
    with open('YaD_token.txt', encoding='utf-8') as f:
        TOKEN = f.readline().strip()
    uploader = YaUploader(TOKEN)
    uploader.upload(path_to_file, name_of_file)
