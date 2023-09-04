# Сервис рассылок

Сервис рассылок - это удобный инструмент для создания и управления рассылками электронных сообщений. 
Наш сервис предоставляет пользователям возможность легко создавать и 
отправлять персонализированные рассылки электронных писем своим клиентам, подписчикам или пользователям.

## Установка и запуск

1. Клонируйте репозиторий на вашем компьютере:
`git clone https://github.com/Lisnevskiy/MailingManagementService.git`
2. Установите зависимости:
`pip install -r requirements.txt`
3. Выполните миграции базы данных:
`python manage.py migrate`
4. Наполение БД с помощью фикстур: `python manage.py loaddata blogs_data.json`
5. Запустите сервер:
`python manage.py runserver`
6. Необходимые примеры переменных окружения указаны в файле [.env.sample](.env.sample)

## Дополнительно

- Запуск брокера: `sudo service redis-server start`
([инструкция для windows](https://redis.io/docs/getting-started/installation/install-redis-on-windows/))
---
