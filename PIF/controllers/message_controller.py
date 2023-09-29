from flask import request, jsonify
from ..models.message_model import create_message, get_message_by_id, update_message, delete_message

# Crear un nuevo mensaje
def create():
    data = request.json
    id_user = data['id_user']
    id_channel = data['id_channel']
    content = data['content']

    message_id = create_message(id_user, id_channel, content)

    return jsonify({"message": "Mensaje creado exitosamente", "message_id": message_id}), 201

# Obtener un mensaje por su ID
def get_by_id(message_id):
    message = get_message_by_id(message_id)
    if message:
        return jsonify(message), 200
    else:
        return jsonify({"message": "Mensaje no encontrado"}), 404

# Actualizar un mensaje por su ID
def update(message_id):
    data = request.json
    content = data['content']

    if update_message(message_id, content):
        return jsonify({"message": "Mensaje actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo actualizar el mensaje"}), 404

# Eliminar un mensaje por su ID
def delete(message_id):
    if delete_message(message_id):
        return jsonify({"message": "Mensaje eliminado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo eliminar el mensaje"}), 404
