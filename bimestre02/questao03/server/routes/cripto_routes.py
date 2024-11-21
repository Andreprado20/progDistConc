from flask import Blueprint, request, jsonify
from models import Criptoativo, Base

# Blueprint para as rotas de criptoativos
cripto_routes = Blueprint("cripto_routes", __name__)

@cripto_routes.route("/criptoativos", methods=["GET"])
def listar_criptoativos():
    """
    Lista todos os criptoativos.
    """
    criptoativos = Criptoativo.query.all()
    resultado = [
        {"id": c.id, "nome": c.nome, "codigo": c.codigo, "preco": c.preco}
        for c in criptoativos
    ]
    return jsonify(resultado), 200


@cripto_routes.route("/criptoativos/<int:id>", methods=["GET"])
def obter_criptoativo(id):
    """
    Obtém os detalhes de um criptoativo pelo ID.
    """
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"erro": "Criptoativo não encontrado"}), 404
    return jsonify(
        {"id": criptoativo.id, "nome": criptoativo.nome, "codigo": criptoativo.codigo, "preco": criptoativo.preco}
    ), 200


@cripto_routes.route("/criptoativos", methods=["POST"])
def criar_criptoativo():
    """
    Cria um novo criptoativo.
    """
    dados = request.json
    if not dados or not all(k in dados for k in ("nome", "codigo", "preco")):
        return jsonify({"erro": "Dados inválidos"}), 400

    novo_criptoativo = Criptoativo(nome=dados["nome"], codigo=dados["codigo"], preco=dados["preco"])
    Base.session.add(novo_criptoativo)
    Base.session.commit()
    return jsonify({"mensagem": "Criptoativo criado com sucesso", "id": novo_criptoativo.id}), 201


@cripto_routes.route("/criptoativos/<int:id>", methods=["PUT"])
def atualizar_criptoativo(id):
    """
    Atualiza os dados de um criptoativo.
    """
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"erro": "Criptoativo não encontrado"}), 404

    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    criptoativo.nome = dados.get("nome", criptoativo.nome)
    criptoativo.codigo = dados.get("codigo", criptoativo.codigo)
    criptoativo.preco = dados.get("preco", criptoativo.preco)
    Base.session.commit()
    return jsonify({"mensagem": "Criptoativo atualizado com sucesso"}), 200


@cripto_routes.route("/criptoativos/<int:id>", methods=["DELETE"])
def excluir_criptoativo(id):
    """
    Exclui um criptoativo.
    """
    criptoativo = Criptoativo.query.get(id)
    if not criptoativo:
        return jsonify({"erro": "Criptoativo não encontrado"}), 404

    Base.session.delete(criptoativo)
    Base.session.commit()
    return jsonify({"mensagem": "Criptoativo excluído com sucesso"}), 200
