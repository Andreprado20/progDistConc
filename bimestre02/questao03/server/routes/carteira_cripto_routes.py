from flask import Blueprint, request, jsonify
from models import CarteiraCripto
from database import db_session

carteira_cripto_bp = Blueprint('carteira_cripto', __name__)

@carteira_cripto_bp.route('/carteira_cripto', methods=['GET'])
def get_carteira_cripto():
    carteira_cripto = CarteiraCripto.query.all()
    return jsonify([cc.__dict__ for cc in carteira_cripto if '_sa_instance_state' not in cc.__dict__])

@carteira_cripto_bp.route('/carteira_cripto', methods=['POST'])
def create_carteira_cripto():
    data = request.json
    carteira_cripto = CarteiraCripto(**data)
    db_session.add(carteira_cripto)
    db_session.commit()
    return jsonify({"message": "CarteiraCripto created"}), 201

@carteira_cripto_bp.route('/carteira_cripto', methods=['DELETE'])
def delete_carteira_cripto():
    id_carteira = request.args.get('id_carteira')
    id_criptoativo = request.args.get('id_criptoativo')
    carteira_cripto = CarteiraCripto.query.filter_by(id_carteira=id_carteira, id_criptoativo=id_criptoativo).first()
    if not carteira_cripto:
        return jsonify({"error": "Not found"}), 404
    db_session.delete(carteira_cripto)
    db_session.commit()
    return jsonify({"message": "CarteiraCripto deleted"})
