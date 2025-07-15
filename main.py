from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

ListaDeProdutos = {
    "sofa": "R$ 1.500,00",
    "sofá": "R$ 1.500,00",
    "mesa": "R$ 700,00",
    "cadeira": "R$ 250,00"
}

def Responder(pergunta):
    pergunta = pergunta.lower()

    for produto in ListaDeProdutos:
        if produto in pergunta:
            return f"O preço do(a) {produto.title()} é {ListaDeProdutos[produto]}."
#Aqui pensei em pessoas que provavelmente irão escrever certo e errado, então para não gerar um looping
    if "preço" in pergunta or "preco" in pergunta or "presso" in pergunta:
        return "De qual produto você gostaria de saber o preço?"

    respostas = {
        "1": "Certo, como posso ajudar?",
        "2": "Até logo!",
        "bom dia": "Bom dia! Em que posso te ajudar?"
    }

    return respostas.get(pergunta, "Desculpe, não entendi sua pergunta.")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")  # carrega o HTML da raiz

@app.route("/chat", methods=["POST"])
def chat():
    print("Olá, \n1 - Para iniciar o atendimento\n2- Encerrar o atendimento")
    dados = request.get_json()
    pergunta = dados.get("mensagem", "")
    resposta = Responder(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
