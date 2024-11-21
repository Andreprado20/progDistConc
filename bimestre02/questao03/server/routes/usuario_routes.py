from flask import Blueprint, request, jsonify
from models import Usuario
from database import db_session

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.__dict__ for u in usuarios if '_sa_instance_state' not in u.__dict__])

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Not found"}), 404
    return jsonify({k: v for k, v in usuario.__dict__.items() if k != '_sa_instance_state'})

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = Usuario(**data)
    db_session.add(usuario)
    db_session.commit()
    return jsonify({"message": "Usuario created"}), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(usuario, key, value)
    db_session.commit()
    return jsonify({"message": "Usuario updated"})

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Not found"}), 404
    db_session.delete(usuario)
    db_session.commit()
    return jsonify({"message": "Usuario deleted"})
