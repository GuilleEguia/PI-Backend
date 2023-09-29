from flask import request, jsonify
from ..models.server_model import create_server, get_server_by_id, update_server, delete_server

# Crear un nuevo servidor
def create():
    data = request.json
    name = data['name']
    description = data.get('description', None)

    server_id = create_server(name, description)

    return jsonify({"message": "Servidor creado exitosamente", "server_id": server_id}), 201

# Obtener un servidor por su ID
def get_by_id(server_id):
    server = get_server_by_id(server_id)
    if server:
        return jsonify(server), 200
    else:
        return jsonify({"message": "Servidor no encontrado"}), 404

# Actualizar un servidor por su ID
def update(server_id):
    data = request.json
    name = data['name']
    description = data.get('description', None)

    if update_server(server_id, name, description):
        return jsonify({"message": "Servidor actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo actualizar el servidor"}), 404

# Eliminar un servidor por su ID
def delete(server_id):
    if delete_server(server_id):
        return jsonify({"message": "Servidor eliminado exitosamente"}), 200
    else:
        return jsonify({"message": "No se pudo eliminar el servidor"}), 404
