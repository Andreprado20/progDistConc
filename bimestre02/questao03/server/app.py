from flask import Flask
from config import Config
from models import Base
from routes.carteira_routes import carteira_bp
from routes.cripto_routes import cripto_routes
from routes.transacao_routes import transacao_routes

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar SQLAlchemy
Base.init_app(app)

# Registrar Blueprints
app.register_blueprint(carteira_bp)
app.register_blueprint(cripto_routes)
app.register_blueprint(transacao_routes)

if __name__ == '__main__':
    app.run(debug=True)
