import mysql.connector
from mysql.connector import Error
from flask import current_app

def create_message(id_user, id_channel, content):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO mensajes (id_usuario, id_canal, contenido)
            VALUES (%s, %s, %s)
        """, (id_user, id_channel, content))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_message_by_id(message_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mensajes WHERE id_mensaje = %s", (message_id,))
        message = cursor.fetchone()
        return message
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update_message(message_id, content):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE mensajes
            SET contenido = %s
            WHERE id_mensaje = %s
        """, (content, message_id))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()

def delete_message(message_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM mensajes WHERE id_mensaje = %s", (message_id,))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()
