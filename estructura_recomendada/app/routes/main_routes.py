# Vamos a crear rutas principales

from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

# Ruta raiz
@main.route('/', methods=['GET'])
def index():
  return jsonify({"mensaje": "Hello World :)"})