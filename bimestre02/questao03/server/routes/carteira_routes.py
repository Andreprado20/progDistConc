from flask import Blueprint, request, jsonify
from models import Base, Carteira

carteira_bp = Blueprint('carteira', __name__)

@carteira_bp.route('/carteiras', methods=['GET'])
def listar_carteiras():
    carteiras = Carteira.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome, 'id_usuario': c.id_usuario} for c in carteiras])

@carteira_bp.route('/carteiras', methods=['POST'])
def criar_carteira():
    dados = request.json
    nova_carteira = Carteira(nome=dados['nome'], id_usuario=dados['id_usuario'])
    Base.session.add(nova_carteira)
    Base.session.commit()
    return jsonify({'message': 'Carteira criada com sucesso!'}), 201
