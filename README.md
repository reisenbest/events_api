# events_api
СПБ ГБУ test task


REST API сервис + чат. Тестовое задание стек - джанго, докер, постгрес, Инструкции к деплою:

скачать\склонировать репозиторий

запустить команду docker-compose up --build из директории где хранится Dockerfile установятся зависимости автоматически пройдут миграции создастся суперюзер запустится сервер

логи для входа:  email = 'admin@admin.com' password = 'admin' username = 'admin'

или авторизоваться через админ панель

jwt токен по api\login\ или через api\token\

мероприятия лучше добавлять через админ-панель, но эндпоинт есть 

В сваггре представлены все эндпоинты

ЧАТ:
при запуске докера автоматически создается комната с именем test, можно свои создать. для каждой своя история сообщений

/chat/ - по этому адресу можно ввести название чат-комнаты и если она есть и пользователь имеет права - перейдет в нее.

