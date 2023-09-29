from flask import Blueprint
from ..controllers.server_controller import ServerController

bp_servers = Blueprint("servers", __name__)

bp_servers.route("/", methods=["GET"])(ServerController.get)
bp_servers.route("/<int:server_id>", methods=["GET"])(ServerController.get_by_id)
bp_servers.route("/", methods=["POST"])(ServerController.create)
bp_servers.route("/<int:server_id>", methods=["PUT"])(ServerController.update)
bp_servers.route("/<int:server_id>", methods=["DELETE"])(ServerController.delete)
