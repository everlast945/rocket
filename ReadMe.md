
БД оставил `sqlite` (для простоты), обычно использую на всех проектах `postgres`.


Для запуска проекта требуется:
- В модуль rocket добавить файл .env c содержимым:
```
DEBUG=on
SECRET_KEY='ASDasdas_asd_dasd$@#%@#%'
```
- Создать виртуальное окружение/активировать его
- Установить пакеты из `requirements.txt`
- Выполнить `python manage.py migrate`
- Можно заполнить БД тестовыми данными выполнив `python manage.py init_empty_base`
- Авторизоваться тут: `api-auth/login/`


Урлы:
- `regions/` - регионы (GET-список древовидный, POST-создание)
- `regions/:region_id/` - регион (PUT/PATCH-редактирование, DELETE-удаление)
- `regions/:region_id/towns/` - города региона (GET-список)
- `regions/:region_id/` - все города (GET-список, POST-создание)
