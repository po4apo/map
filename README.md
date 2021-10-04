# Тестовое задание на должность Back-end для компании MediaSoft.

## О проеткте: API для простой базы данных

## Задание:

### Функционал:

1. В случае успешной обработки сервис должен отвечать статусом 200, в
   случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.
3. Запросы:
   1. GET /city/ — получение всех городов из базы;
   2. GET /city//street/ — получение всех улиц города; (city_id —
      идентификатор города)
      c. POST /shop/ — создание магазина; Данный метод получает json c
      объектом магазина, в ответ возвращает id созданной записи.
4. GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
   1. Метод принимает параметры для фильтрации. Параметры не
      обязательны. В случае отсутствия параметров выводятся все
      магазины, если хоть один параметр есть , то по нему
      выполняется фильтрация.
   2. Важно!: в объекте каждого магазина выводится название
      города и улицы, а не id записей.
   3. Параметр open: 0 - закрыт, 1 - открыт. Данный статус
      определяется исходя из параметров «Время открытия»,
      «Время закрытия» и текущего времени сервера.

### Объекты:

#### Магазин:

* Название
* Город
* Улица
* Дом
* Время открытия
* Время закрытия

#### Город:

* Название

####Улица:

* Название
* Город

## Инструкция установки:

1. Установите virtualenv `python3 -m venv env`
2. Скачайте проект `git clone https://github.com/po4apo/map.git`
3. Перейдите в папку map
4. Установите requirements.txt `pip install -r requirements.txt`
5. Перейдите map/setting.py
6. Добавьте базу данных

   ```DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql_psycopg2',
   'NAME': 'название вашей бд',
   'USER': 'имя пользователя',
   'PASSWORD': 'пароль',
   'HOST': '127.0.0.1',
   'PORT': '5432',
   }
   }
   ```
7. Запустите сервер `python manage.py runserver`
