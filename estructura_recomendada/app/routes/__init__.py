from .user_routes import user
from .main_routes import main
def register_routes(app):
  app.register_blueprint(user)
  app.register_blueprint(main)