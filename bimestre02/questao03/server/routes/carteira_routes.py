from flask import Blueprint, request, jsonify
from models import Carteira
from database import db_session

carteira_bp = Blueprint('carteira', __name__)

@carteira_bp.route('/carteiras', methods=['GET'])
def get_carteiras():
    carteiras = Carteira.query.all()
    return jsonify([c.__dict__ for c in carteiras if '_sa_instance_state' not in c.__dict__])

@carteira_bp.route('/carteiras/<int:id>', methods=['GET'])
def get_carteira(id):
    carteira = Carteira.query.get(id)
    if not carteira:
        return jsonify({"error": "Not found"}), 404
    return jsonify({k: v for k, v in carteira.__dict__.items() if k != '_sa_instance_state'})

@carteira_bp.route('/carteiras', methods=['POST'])
def create_carteira():
    data = request.json
    carteira = Carteira(**data)
    db_session.add(carteira)
    db_session.commit()
    return jsonify({"message": "Carteira created"}), 201

@carteira_bp.route('/carteiras/<int:id>', methods=['PUT'])
def update_carteira(id):
    carteira = Carteira.query.get(id)
    if not carteira:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(carteira, key, value)
    db_session.commit()
    return jsonify({"message": "Carteira updated"})

@carteira_bp.route('/carteiras/<int:id>', methods=['DELETE'])
def delete_carteira(id):
    carteira = Carteira.query.get(id)
    if not carteira:
        return jsonify({"error": "Not found"}), 404
    db_session.delete(carteira)
    db_session.commit()
    return jsonify({"message": "Carteira deleted"})
