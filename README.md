# Auth microservice
Микровервис для аутентификации в "Цифровом двойнике".

## Разработано с помощью:
- Python 3.11
- FastAPI
- PostgreSQL 
- SQLAlchemy v2
- Pydantic v2

## Сборка и запуск проекта:
    git clone https://github.com/AgroScience-Team/auth-service.git
    
Из корневой папки проекта:

    docker-compose up -d 

Swagger: `http://0.0.0.0:8000/docs`

## Работа в Swagger:

При переходе на:
`http://0.0.0.0:8000/docs` будут доступны текущие эндпоинты. Для работы с некоторыми из них, требуется аутентификация/авторизация (такие эндпоинты помечены значком 🔓). 

- В правом верхнем углу есть кнопка `Authorize`, генерирующая форму для аутентификации.

- При успешной аутентификации, значки защищенных эндпоинтов меняются на 🔒, и теперь, вы можете тестировать защищенные эндпоинты (в заголовки запросов автоматически добаляется JWToken, сгенерированный на этапе аутентификации).

