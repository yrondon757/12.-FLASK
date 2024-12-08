# Vamos a crear rutas para los usuarios

from flask import Blueprint, jsonify, request

# Vamos a importar los controladores
from app.controllers.user_controller import get_users, get_user, get_user_query, create_user, update_user, delete_user

user = Blueprint('user', __name__)

# Ruta para obtener todos los usuarios
@user.route('/users', methods=['GET'])
def get_all_users():
  return jsonify(get_users())

# Ruta para obtener un usuario a traves de su ID
@user.route('/users/<user_id>', methods=['GET'])
def get_one_user(user_id):
  return jsonify(get_user(user_id))

# Ruta para obtener el valor del id desde los parametros de la consulta (query parameters)
@user.route('/users/query', methods=['GET'])
def get_one_user_query():
  # Para obtener estos valores (variables) desde los query debemos hacer lo siguiente
  user_id = request.args.get('user_id')
  return jsonify(get_user_query(user_id))

# Ruta para crear un usuario
@user.route('/users', methods=['POST'])
def add_user():
  return jsonify(create_user(request.json))

# Ruta para actualizar un usuario
@user.route('/users/<user_id>', methods=['PATCH'])
def update_user_id(user_id):
  return jsonify(update_user(user_id, request.json))

# Ruta para eliminar un usuario
@user.route('/users/<user_id>', methods=['DELETE'])
def eliminate_user(user_id):
  return jsonify(delete_user(user_id))