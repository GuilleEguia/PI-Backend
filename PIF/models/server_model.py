import mysql.connector
from mysql.connector import Error
from flask import current_app

def create_server(name, description):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO servidores (nombre, descripcion)
            VALUES (%s, %s)
        """, (name, description))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_server_by_id(server_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servidores WHERE id_servidor = %s", (server_id,))
        server = cursor.fetchone()
        return server
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update_server(server_id, name, description):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE servidores
            SET nombre = %s, descripcion = %s
            WHERE id_servidor = %s
        """, (name, description, server_id))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()

def delete_server(server_id):
    try:
        conn = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM servidores WHERE id_servidor = %s", (server_id,))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()
