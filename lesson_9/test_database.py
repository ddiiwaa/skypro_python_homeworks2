import pytest 
from sqlalchemy import create_engine, text, Column, INTEGER, String
import psycopg2 

db_connection_string = "postgresql://postgres:2335108@localhost:5432/mydatabase"
db = create_engine(db_connection_string)

def test_insert():
    # Создаём соединение
    with db.connect() as connection:
        sql = text("INSERT INTO users (user_email) VALUES (:new_user)")
        # Выполняем запрос через соединение
        result = connection.execute(sql, {"new_user": "http://123galashlist.ru"})
        print(f"Rows affected: {result.rowcount}")

def test_update():
    db = create_engine(db_connection_string)
    with db.connect() as connection:
        sql = text("UPDATE users SET user_email = :email WHERE user_email = :user_email")
        result = connection.execute(sql, {"email": "new123galash@list.ru", "user_email": "123galash@list.ru"})
        print(f"Rows affected (update): {result.rowcount}")

def test_delete():
    db = create_engine(db_connection_string)
    with db.connect() as connection:
        sql = text("DELETE FROM users WHERE user_email = :email")
        result = connection.execute(sql, {"email": "new123galash@list.ru"})
        print(f"Rows affected (delete): {result.rowcount}")
