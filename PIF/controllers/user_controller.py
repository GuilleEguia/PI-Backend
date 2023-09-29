from flask import request, jsonify
from ..models.user_model import create_user, get_user_by_id, update_user, delete_user, login_user

# Crear un nuevo usuario
def create():
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']

    user_id = create_user(username, password, email)

    return jsonify({"message": "Usuario creado exitosamente", "user_id": user_id}), 201

# Obtener un usuario por su ID
def get_by_id(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404

# Actualizar un usuario por su ID
def update(user_id):
    data = request.json
    username = data['username']
    password = data['password']
    email = data['email']

    if update_user(user_id, username, password, email):
        return jsonify({"message": "Usuario actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo actualizar el usuario"}), 404

# Eliminar un usuario por su ID
def delete(user_id):
    if delete_user(user_id):
        return jsonify({"message": "Usuario eliminado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo eliminar el usuario"}), 404

# Iniciar sesión de usuario
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = login_user(username, password)

    if user:
        return jsonify({"message": "Inicio de sesión exitoso", "user_id": user['id_usuario']}), 200
    else:
        return jsonify({"message": "Credenciales de inicio de sesión incorrectas"}), 401
