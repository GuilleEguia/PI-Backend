from flask import request, jsonify
from ..models.channel_model import create_channel, get_channel_by_id, update_channel, delete_channel

# Crear un nuevo canal
def create():
    data = request.json
    id_server = data['id_server']
    name = data['name']
    description = data.get('description', None)

    channel_id = create_channel(id_server, name, description)

    return jsonify({"message": "Canal creado exitosamente", "channel_id": channel_id}), 201

# Obtener un canal por su ID
def get_by_id(channel_id):
    channel = get_channel_by_id(channel_id)
    if channel:
        return jsonify(channel), 200
    else:
        return jsonify({"message": "Canal no encontrado"}), 404

# Actualizar un canal por su ID
def update(channel_id):
    data = request.json
    name = data['name']
    description = data.get('description', None)

    if update_channel(channel_id, name, description):
        return jsonify({"message": "Canal actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo actualizar el canal"}), 404

# Eliminar un canal por su ID
def delete(channel_id):
    if delete_channel(channel_id):
        return jsonify({"message": "Canal eliminado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo eliminar el canal"}), 404
