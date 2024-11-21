from flask import Flask
from routes.criptoativo_routes import criptoativo_bp
from routes.usuario_routes import usuario_bp
from routes.carteira_routes import carteira_bp
from routes.carteira_cripto_routes import carteira_cripto_bp
from routes.transacao_routes import transacao_bp

app = Flask(__name__)

# Register blueprints with specific prefixes
app.register_blueprint(criptoativo_bp, url_prefix='/api/criptoativos')
app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
app.register_blueprint(carteira_bp, url_prefix='/api/carteiras')
app.register_blueprint(carteira_cripto_bp, url_prefix='/api/carteira_cripto')
app.register_blueprint(transacao_bp, url_prefix='/api/transacoes')

if __name__ == '__main__':
    app.run(debug=True)
