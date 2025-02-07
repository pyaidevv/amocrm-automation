
# AmoCRM Automation

Этот проект представляет собой веб-хук для автоматизации работы с AmoCRM, используя Flask.

## Описание

Этот веб-сервис принимает POST-запросы, извлекает данные о лидах, а затем обновляет соответствующее поле в AmoCRM через API.

## Требования

Перед началом работы убедитесь, что у вас установлен Python 3 и следующие зависимости:

```bash
pip install flask requests python-dotenv
```

## Установка и настройка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/amocrm-automation.git
cd amocrm-automation
```

2. Создайте файл `.env` в корневой папке и добавьте в него:

```
AMOCRM_DOMAIN=ewfewfe.amocrm.ru
ACCESS_TOKEN=your_access_token
CUSTOM_FIELD_ID=fewfewf29
```

3. Запустите сервер:

```bash
python app.py
```

Сервер запустится на `http://0.0.0.0:5001`.

## Использование

Отправьте POST-запрос на `/webhook` с данными в теле запроса. Пример:

```json
{
  "unsorted[add][0][lead_id]": "123456",
  "unsorted[add][0][source_data][client][id]": "654321"
}
```

## Развертывание

Для продакшн-использования рекомендуется развернуть сервер с помощью Gunicorn или Docker.

## Лицензия

Этот проект распространяется под лицензией MIT.
