# Менеджер паролей
Простой менеджер паролей с использованием базы данных SQLite и графическим интерфейсом PyQt5.
Присутствует авторизация. Пароли хешируются ресурсозатратной функцией PBKDF2.
Все записи пользователя шифруются. Для шифровки используется ключ, получаемый из пароля пользователя при авторизации. Поэтому, не помнишь пароль - попрощайся со всей информацией (L). Никаких "Забыли пароль?" тут нет. 

TODO: добавить возможность записи/чтения БД в Google Drive
