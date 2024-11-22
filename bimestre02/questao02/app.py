from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dados simples
users = {
    "astrologoCanadense": {"nickname": "astrologoCanadense666", "plan": "basic"},
    "mestreZodiaco": {"nickname": "mestreZodiaco", "plan": "advanced"},
}

horoscopes = {
    "aries": {"message": "A energia está a seu favor hoje!", "lucky_number": 12},
    "touro": {"message": "Evite decisões impulsivas.", "lucky_number": 7},
    "sagitario":{"message": "Todos os astros se alinharam ao seu favor!", "lucky_number": 20}
    # Adicione outros signos aqui...
}

# Rota de autenticação simples
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    nickname = data.get('nickname')
    user = users.get(nickname)
    if user:
        return jsonify({"success": True, "message": "Usuário autenticado!", "plan": user["plan"]}), 200
    return jsonify({"success": False, "message": "Usuário não encontrado!"}), 404

# Rota para consultar o horóscopo
@app.route('/horoscope', methods=['POST'])
def get_horoscope():
    data = request.json
    nickname = data.get('nickname')
    sign = data.get('sign')
    
    user = users.get(nickname)
    if not user:
        return jsonify({"success": False, "message": "Usuário não autenticado!"}), 403
    
    horoscope = horoscopes.get(sign.lower())
    if not horoscope:
        return jsonify({"success": False, "message": "Signo inválido!"}), 404
    
    response = {"message": horoscope["message"]}
    if user["plan"] == "advanced":
        response["lucky_number"] = horoscope["lucky_number"]
    
    return jsonify({"success": True, "data": response}), 200

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    nickname = data.get('nickname')
    plan = data.get('plan', 'basic')  # O plano padrão é 'basic'
    
    if not nickname or nickname in users:
        return jsonify({"success": False, "message": "Nickname inválido ou já existente!"}), 400
    
    users[nickname] = {"nickname": nickname, "plan": plan}
    return jsonify({"success": True, "message": "Usuário criado com sucesso!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
