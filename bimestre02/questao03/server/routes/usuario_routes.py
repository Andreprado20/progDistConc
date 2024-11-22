from flask import Flask, Blueprint, request, jsonify
from database import get_db_connection

usuario_bp = Blueprint('usuario', __name__)

# GET endpoint to retrieve all users
@usuario_bp.route('/usuarios', methods=['GET'])
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
@usuario_bp.route('/usuarios', methods=['POST'])
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