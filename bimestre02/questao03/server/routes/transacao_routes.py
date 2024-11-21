from flask import Blueprint, request, jsonify
from models import Carteira, Criptoativo, Base
from datetime import datetime

# Blueprint para as rotas de transações
transacao_routes = Blueprint("transacao_routes", __name__)

@transacao_routes.route("/transacoes/compra", methods=["POST"])
def comprar_cripto():
    """
    Realiza a compra de um criptoativo para uma carteira.
    """
    dados = request.json
    if not dados or not all(k in dados for k in ("id_carteira", "id_criptoativo", "quantidade")):
        return jsonify({"erro": "Dados inválidos"}), 400

    carteira = Carteira.query.get(dados["id_carteira"])
    criptoativo = Criptoativo.query.get(dados["id_criptoativo"])
    if not carteira or not criptoativo:
        return jsonify({"erro": "Carteira ou criptoativo não encontrado"}), 404

    custo_total = criptoativo.preco * dados["quantidade"]
    if carteira.saldo < custo_total:
        return jsonify({"erro": "Saldo insuficiente"}), 400

    carteira.saldo -= custo_total
    Base.session.commit()

    # Registro no histórico (opcional)
    # Aqui você pode adicionar um modelo e registrar a transação

    return jsonify({"mensagem": "Compra realizada com sucesso"}), 200


@transacao_routes.route("/transacoes/venda", methods=["POST"])
def vender_cripto():
    """
    Realiza a venda de um criptoativo de uma carteira.
    """
    dados = request.json
    if not dados or not all(k in dados for k in ("id_carteira", "id_criptoativo", "quantidade")):
        return jsonify({"erro": "Dados inválidos"}), 400

    carteira = Carteira.query.get(dados["id_carteira"])
    criptoativo = Criptoativo.query.get(dados["id_criptoativo"])
    if not carteira or not criptoativo:
        return jsonify({"erro": "Carteira ou criptoativo não encontrado"}), 404

    # Para venda, supõe-se que existe um controle de quantidade de criptoativos na carteira.
    # Este código considera que o registro existe e a quantidade será reduzida.
    # Verifique e implemente o controle de quantidade caso necessário.

    valor_total = criptoativo.preco * dados["quantidade"]
    carteira.saldo += valor_total
    Base.session.commit()

    return jsonify({"mensagem": "Venda realizada com sucesso"}), 200


@transacao_routes.route("/transacoes/transferencia", methods=["POST"])
def transferir_cripto():
    """
    Transfere criptoativos entre duas carteiras.
    """
    dados = request.json
    if not dados or not all(k in dados for k in ("id_origem", "id_destino", "id_criptoativo", "quantidade")):
        return jsonify({"erro": "Dados inválidos"}), 400

    carteira_origem = Carteira.query.get(dados["id_origem"])
    carteira_destino = Carteira.query.get(dados["id_destino"])
    criptoativo = Criptoativo.query.get(dados["id_criptoativo"])

    if not carteira_origem or not carteira_destino or not criptoativo:
        return jsonify({"erro": "Carteira ou criptoativo não encontrado"}), 404

    # Verifique se a carteira de origem possui a quantidade necessária do criptoativo.
    # Este código assume que existe um controle disso.

    # Realiza a transferência
    Base.session.commit()

    return jsonify({"mensagem": "Transferência realizada com sucesso"}), 200


@transacao_routes.route("/transacoes/historico/<int:id_carteira>", methods=["GET"])
def historico_transacoes(id_carteira):
    """
    Retorna o histórico de transações de uma carteira específica.
    """
    carteira = Carteira.query.get(id_carteira)
    if not carteira:
        return jsonify({"erro": "Carteira não encontrada"}), 404

    # Este exemplo assume que existe uma tabela ou modelo para armazenar o histórico.
    # Exemplo de formato:
    # historico = Transacao.query.filter_by(id_carteira=id_carteira).all()
    # resultados = [{"id": t.id, "tipo": t.tipo, "quantidade": t.quantidade, "data": t.data} for t in historico]

    resultados = []  # Substitua por consulta real
    return jsonify(resultados), 200
