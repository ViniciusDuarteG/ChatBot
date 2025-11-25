from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ListaDeProdutos = {
    "sofa": "R$ 1.500,00",
    "sofá": "R$ 1.500,00",
    "mesa": "R$ 700,00",
    "cadeira": "R$ 250,00"
}
#nessa função colocar as respostas é crucial
#lembre-se que utilizar o if ou a biblioteca para situações diferentes
def Responder(pergunta):
    pergunta = pergunta.lower()

    for produto in ListaDeProdutos:
        if produto in pergunta:
            return f"O preço do(a) {produto.title()} é {ListaDeProdutos[produto]}."

    if "preço" in pergunta or "preco" in pergunta or "presso" in pergunta or "preso" in pergunta:
        return "De qual produto você gostaria de saber o preço?"
    
    if "qual o seu objetivo" in pergunta or "faz" in pergunta: 
        return "Sou um chatbot demonstrativo, possuo uma quantidade limitada de interações. Posso responder dados, como uma pequena lista de produtos de casaque eu tenho, como uma cama, um sofá e uma mesa."

    if "desenvolveu" in pergunta or "desenvolvedor" in pergunta or "dev" in pergunta:
        return "Bom, fui desenvolvido por Vinicius Duarte, pode contacta-lo pelo LinkedIn ou pelo Github que estão no roda-pé da página."

    respostas = {
        "1": "Certo, como posso ajudar?",
        "2":"Sou um chatBot desenvolvido por Vinícius Duarte, meu objetivo é simular um atendimento real de um marketplace, porém posso ser utilizado para outros objetivos",
        "0": "Até logo!",
        "bom dia": "Olá! Em que posso te ajudar?",
        "oi":"Olá! Em que posso te ajudar?",
        "olá":"Olá! Em que posso te ajudar?",
        "boa tarde":"Olá! Em que posso te ajudar?",
        "boa noite":"Olá! Em que posso te ajudar?",
        "ola":"Olá! Em que posso te ajudar?",
    }

    return respostas.get(pergunta, "Desculpe, não entendi sua pergunta.")

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/chat", methods=["POST"])
def chat():
    print("Olá, \n1 - Para iniciar o atendimento\n2 - Informações para o usuário\n0 - Encerrar o atendimento")
    dados = request.get_json()
    pergunta = dados.get("mensagem", "")
    resposta = Responder(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
