# Kaluga urban environment bot

Телеграм бот для проекта "Городская среда" города Калуги

## Запуск бота

Для запуска бота нужны следующие параметры окружения:

* `BOT_TOKEN` - токен телеграм бота
* `BOT_ADMINS` - список администраторов бота: строка со списком`telegram_id`, разделенных через запятую (Например, '123456, 654321')
* `DB_CONNECTION_STRING` - строка подключения к БД (по умолчанию: 'sqlite:///local.db'). Формат строк подключения можете посмотреть [тут](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html?highlight=connection%20string#database-url)

Локально запускается командой:

```shell
python main.py
```
