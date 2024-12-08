# Vamos a importar Flask y MySQL
from flask import Flask
from flask_mysqldb import MySQL
# Vamos a importar los datos de MYSQL
from .config import Config

# Vamos a importar CORS : pip install flask-cors
from flask_cors import CORS

mysql = MySQL()

def create_app():
  app = Flask(__name__)
  allowed_origins = ['*']
  CORS(app, resources={r"/*": {"origins": allowed_origins}})
  #CORS(app)
  app.config.from_object(Config)
  
  # iniciamos el servicio de MySQL
  mysql.init_app(app)
  
  # Vamos a importar las rutas aqui
  from .routes import register_routes
  register_routes(app)
  
  return app