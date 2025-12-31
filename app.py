from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def Responder(pergunta):
    pergunta = pergunta.lower()

    if "qual o seu objetivo" in pergunta or "o que você faz" in pergunta:
        return (
            "Sou um chatbot demonstrativo criado por Vinicius Duarte. "
            "Posso apresentar seu perfil profissional, habilidades técnicas, "
            "projetos e formas de contato."
        )

    if "desenvolveu" in pergunta or "desenvolvedor" in pergunta or "dev" in pergunta:
        return (
            "Fui desenvolvido por Vinicius Duarte. "
            "Você pode acessar o GitHub dele aqui:\n"
            "https://github.com/SEU_USUARIO"
        )

    if "vinicius" in pergunta:
        return (
            "Vinicius Duarte é desenvolvedor júnior, com foco em sistemas web, "
            "automações e análise de dados. Atua com Python, Flask e banco de dados."
        )

    respostas = {
        "1": (
            "O Vinicius Duarte é desenvolvedor júnior, com experiência em desenvolvimento de sistemas e automações.\n\n"
            "Possui perfil autodidata e está sempre aprimorando suas habilidades."
        ),

        "2": (
            "🖥 Linguagens:\n"
            "- Python\n- JavaScript\n- Pascal\n- Delphi\n- Java\n\n"
            "🌐 Web:\n"
            "- HTML\n- CSS\n- Flask\n- Django\n\n"
            "🗄 Banco de Dados:\n"
            "- MySQL\n- SQLite\n\n"
            "📊 Dados:\n"
            "- Pandas\n- Excel\n- SQL\n\n"
            "📦 Outros:\n"
            "- Git e GitHub\n"
            "- Desenvolvimento de apps com Kivy"
        ),

        "3": (
            "Projetos desenvolvidos incluem sistemas em Python, automação de documentos, aplicações web com Flask e integração com banco de dados."
        ),

        "4": (
            "O Vinicius já atuou profissionalmente com desenvolvimento de sistemas, trabalhando com Python, banco de dados e aplicações web."
            "Participou do desenvolvimento e manutenção de soluções internas e automações no seu ambiente de trabalho, visando sempre otimizar e economizar tempo em tarefas."
        ),

        "5": (
            "O objetivo do Vinicius é atuar como Desenvolvedor Júnior, aprimorar suas habilidades técnicas e crescer profissionalmente."
        ),

        "6": (
            "Você pode entrar em contato com o Vinicius pelos canais abaixo:\n\n"
            "🔗 GitHub:\nhttps://github.com/ViniciusDuarteG\n\n"
            "🔗 LinkedIn:\nhttps://www.linkedin.com/in/vinicius-duarte-348705170/"
        ),

        "bom dia": "Olá! Em que posso te ajudar?",
        "boa tarde": "Olá! Em que posso te ajudar?",
        "boa noite": "Olá! Em que posso te ajudar?",
        "oi": "Olá! Em que posso te ajudar?",
        "olá": "Olá! Em que posso te ajudar?",
        "ola": "Olá! Em que posso te ajudar?"
    }

    return respostas.get(pergunta, "Desculpe, não entendi sua pergunta.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    pergunta = dados.get("mensagem", "")
    resposta = Responder(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
