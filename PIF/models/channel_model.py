import mysql.connector
from mysql.connector import Error
from flask import current_app

def create_channel(id_server, name, description):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO canales (id_servidor, nombre, descripcion)
            VALUES (%s, %s, %s)
        """, (id_server, name, description))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_channel_by_id(channel_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM canales WHERE id_canal = %s", (channel_id,))
        channel = cursor.fetchone()
        return channel
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update_channel(channel_id, name, description):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE canales
            SET nombre = %s, descripcion = %s
            WHERE id_canal = %s
        """, (name, description, channel_id))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()

def delete_channel(channel_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM canales WHERE id_canal = %s", (channel_id,))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()
