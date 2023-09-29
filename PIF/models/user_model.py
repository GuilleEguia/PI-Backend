import mysql.connector
from mysql.connector import Error
from flask import current_app

def create_user(username, password, email):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre_usuario, contrasenia, email)
            VALUES (%s, %s, %s)
        """, (username, password, email))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
        user = cursor.fetchone()
        return user
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update_user(user_id, username, password, email):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE usuarios
            SET nombre_usuario = %s, contrasenia = %s, email = %s
            WHERE id_usuario = %s
        """, (username, password, email, user_id))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()

def delete_user(user_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (user_id,))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()
