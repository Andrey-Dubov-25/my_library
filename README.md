### Проект MyLibrary

## Описание проекта
MyLibrary - это проект для управления книгами.


**В проекте доступно**:
- создание книг;
- получение книг;
- редактирование книг;
- удаление книг


## Используемые технологии
*Проект реализован с использованием следующего функционала*: 
- Python 3.12
- FastAPI 0.138.2

Все необходимые для работы Foodgram зависимости перечислены в requirements.txt
Рекомендуется перед установкой развернуть виртуальное окружение с верисей python 3.12:

Bash:
```
py -3.12 -m venv venv 
```

Для установки зависимостей необходимо выполнить установку зависимостей:
```
pip install -r requirements.txt
```


## Примеры запросов

**Получение книги**
```
GET /books/{book_id}

```

```
Content type: application/json

{
  "title": "string",
  "author": "string",
  "year": 1000,
  "pages": 11,
  "is_read": false,
  "id": 0
}
```

200 - Удачное выполнение запроса 
404 - Страница не найдена

**Создание книги**

```
POST /books/
```

```
{
  "title": "string",
  "author": "string",
  "year": 1000,
  "pages": 11,
  "is_read": false
}
```

201 - Удачное выполнение запроса
400 - Отсутствует обязательно поле или оно некорректно


## Команда проекта
Проект создан в целях изучения возможностей фреймворка FastAPI.  
Над проектом работал [Андрей Дубов](https://github.com/Andrey-Dubov-25)  



## Ссылка на проект
[Проект MyLibrary](https://github.com/Andrey-Dubov-25/my_library)



### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andrey-Dubov-25/my_library
```

```
cd my_library
```


Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```


Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запустить проект:

```
uvicorm main:app --reload
```