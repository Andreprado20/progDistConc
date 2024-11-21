from flask import Blueprint, request, jsonify
from models import Criptoativo
from database import db_session

criptoativo_bp = Blueprint('criptoativo', __name__)

@criptoativo_bp.route('/criptoativos', methods=['GET'])
def get_criptoativos():
    criptoativos = Criptoativo.query.all()
    return jsonify([c.__dict__ for c in criptoativos if '_sa_instance_state' not in c.__dict__])

@criptoativo_bp.route('/criptoativos/<int:id>', methods=['GET'])
def get_criptoativo(id):
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"error": "Not found"}), 404
    return jsonify({k: v for k, v in criptoativo.__dict__.items() if k != '_sa_instance_state'})

@criptoativo_bp.route('/criptoativos', methods=['POST'])
def create_criptoativo():
    data = request.json
    criptoativo = Criptoativo(**data)
    db_session.add(criptoativo)
    db_session.commit()
    return jsonify({"message": "Criptoativo created"}), 201

@criptoativo_bp.route('/criptoativos/<int:id>', methods=['PUT'])
def update_criptoativo(id):
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(criptoativo, key, value)
    db_session.commit()
    return jsonify({"message": "Criptoativo updated"})

@criptoativo_bp.route('/criptoativos/<int:id>', methods=['DELETE'])
def delete_criptoativo(id):
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"error": "Not found"}), 404
    db_session.delete(criptoativo)
    db_session.commit()
    return jsonify({"message": "Criptoativo deleted"})
