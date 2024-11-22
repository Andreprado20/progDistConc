from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
from carteira_routes import carteira_bp
from database import get_db_connection
from criptoativo_routes import criptoativo_bp
from usuario_routes import usuario_bp


# Load environment variables
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize Flask app
app = Flask(__name__)

app.register_blueprint(carteira_bp, url_prefix='/api')
app.register_blueprint(criptoativo_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/api')

# Database connection helper
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
#         return conn
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")
#         return None

# GET endpoint to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM usuario;")
            users = cur.fetchall()
        conn.close()
        return jsonify(users), 200
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

# POST endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    nome = data.get("nome")
    login = data.get("login")
    senha = data.get("senha")

    if not nome or not login or not senha:
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO usuario (nome, login, senha)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (nome, login, senha),
            )
            user_id = cur.fetchone()["id"]
            conn.commit()
        conn.close()
        return jsonify({"message": "User added successfully", "id": user_id}), 201
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500
    

@app.route('/carteiras', methods=['GET'])
def get_carteiras():
    carteira_id = request.args.get('id')  # Optional ID query param
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with conn.cursor() as cur:
            if carteira_id:
                cur.execute("SELECT * FROM carteira WHERE id = %s;", (carteira_id,))
                carteira = cur.fetchone()
                if not carteira:
                    return jsonify({"error": "Carteira not found"}), 404
            else:
                cur.execute("SELECT * FROM carteira;")
                carteira = cur.fetchall()
        conn.close()
        return jsonify(carteira), 200
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

# POST: Create a new carteira
@app.route('/carteiras', methods=['POST'])
def create_carteira():
    data = request.get_json()
    nome = data.get("nome")
    id_usuario = data.get("id_usuario")

    if not nome or not id_usuario:
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO carteira (nome, id_usuario) VALUES (%s, %s) RETURNING id;",
                (nome, id_usuario),
            )
            carteira_id = cur.fetchone()["id"]
            conn.commit()
        conn.close()
        return jsonify({"message": "Carteira created successfully", "id": carteira_id}), 201
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
