from flask import Blueprint, request, jsonify
from models import Transacao
from database import db_session

transacao_bp = Blueprint('transacao', __name__)

@transacao_bp.route('/transacoes', methods=['GET'])
def get_transacoes():
    transacoes = Transacao.query.all()
    return jsonify([t.__dict__ for t in transacoes if '_sa_instance_state' not in t.__dict__])

@transacao_bp.route('/transacoes', methods=['POST'])
def create_transacao():
    data = request.json
    transacao = Transacao(**data)
    db_session.add(transacao)
    db_session.commit()
    return jsonify({"message": "Transacao created"}), 201

@transacao_bp.route('/transacoes/<int:id>', methods=['DELETE'])
def delete_transacao(id):
    transacao = Transacao.query.get(id)
    if not transacao:
        return jsonify({"error": "Not found"}), 404
    db_session.delete(transacao)
    db_session.commit()
    return jsonify({"message": "Transacao deleted"})
