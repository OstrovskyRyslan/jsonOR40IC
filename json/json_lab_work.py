import json
import requests

# Завдання 1: Читання JSON з файлу
def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

data = read_json_file('data.json')
print("Вміст файлу data.json:", json.dumps(data, indent=4, ensure_ascii=False))

# Завдання 2: Запис словника у JSON файл
def write_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

dict_data = {
    "ім'я": "Олександр",
    "вік": 30,
    "заміжній": False,
    "навички": ["Python", "JavaScript", "SQL"]
}

write_json_file('output.json', dict_data)
print("Дані збережено у файл output.json")

# Завдання 3: Запит до публічного API та виведення title та body перших 10 постів
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for post in posts[:10]:  # Вивести перші 10 постів
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)
else:
    print("Помилка при отриманні даних з API")
