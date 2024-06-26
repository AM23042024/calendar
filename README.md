# Календарное приложение API
## Описание
Этот проект представляет собой простое API для управления календарными событиями. Вы можете добавлять, просматривать, обновлять и удалять события через HTTP-запросы.
## Запуск проекта
1. Создайте виртуальное окружение:
python -m venv venv
2. Активируйте виртуальное окружение:
- На Windows:
  ```
  venv\Scripts\activate
  ```
- На macOS и Linux:
  ```
  source venv/bin/activate
  ```
3. Установите зависимости:
pip install -r requirements.txt
4. Запустите приложение:
./venv/bin/flask --app ./api.py run
## Тестирование проекта
Вы можете использовать инструмент cURL для тестирования функциональности API. Вот некоторые примеры тестов:
### Добавление нового события
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-04-24|Название события|Описание события"
### Получение списка всех событий
curl http://127.0.0.1:5000/api/v1/calendar/
### Получение события по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/calendar/1/
### Обновление текста события по идентификатору / ID == 1 / Новый текст == "Новое описание события"
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-04-24|Название события|Новое описание события"
### Удаление события по идентификатору / ID == 1
$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted
$ curl http://127.0.0.1:5000/api/v1/calendar/
failed to LIST with: Exception: Событие не найдено в хранилище
