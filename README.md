#Чат бот по тестовому заданию.
Написать программу, которая шлёт в некоторый канал в Телеграмме последнюю новость с сайта https://vc.ru

###Решение

_Для получение новости был создан парсер, который считывет все новости со страницы __https://vc.ru/news/all__ 
и формирует список со словарями из новостей. Для парсинага используется request и bs4_

_Бот для телеграма создан на базе __aiogram__. Для запуска неопходимо создать токен и положить его в файл __config.py___

_Запуск бота идет с файла __main.py___