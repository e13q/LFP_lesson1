# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как использовать

Для работы скрипта необходим установленный Python3.

Используйте `pip` (или `pip3`, если при вызове происходит конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Также, нужен файл с данными wine.xlsx, либо создать .env и указать путь до файла с данными.

Пример заполненной строки в файле .env 
```
XSL_FILEPATH_BEVERAGES = '../wine.xlsx'
```
(файл в примере находится в родительской директории проекта)

## Пример содержания .xlsx файла

|   Категория  |       Название      |       Сорт      | Цена |         Картинка         |         Акция        |
|:------------:|:-------------------:|:---------------:|:----:|:------------------------:|:--------------------:|
| Белые вина   | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки      | Коньяк классический |                 | 350  | konyak_klassicheskyi.png |                      |
| Белые вина   | Ркацители           | Ркацители       | 499  | rkaciteli.png            |                      |
| Красные вина | Черный лекарь       | Качич           | 399  | chernyi_lekar.png        |                      |
| Красные вина | Хванчкара           | Александраули   | 550  | hvanchkara.png           |                      |
| Белые вина   | Кокур               | Кокур           | 450  | kokur.png                |                      |
| Красные вина | Киндзмараули        | Саперави        | 550  | kindzmarauli.png         |                      |
| Напитки      | Чача                |                 | 299  | chacha.png               | Выгодное предложение |
| Напитки      | Коньяк кизиловый    |                 | 350  | konyak_kizilovyi.png     |                      |

Картинки находятся в /images/ корневой директории проекта. 

Для корректного отображения картинок из других директорий необходимо в поле "Картинка" указать полное имя файла картинки.

## Пример запуска

После запуска консоли в директории проекта запускаем проект с помощью команды
```
py main.py
```
либо 
```
python3 main.py
```

В браузере открыть сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
