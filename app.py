from flask import Flask, render_template_string, request, jsonify

app = Flask(_name_)

# Template HTML/CSS/JS integrado para funcionamento direto
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOPE-IA - Tecnologia do Brasil</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        header {
            background-color: #1e293b;
            padding: 1rem 2rem;
            text-align: center;
            border-bottom: 1px solid #334155;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        header h1 {
            color: #38bdf8;
            font-size: 1.5rem;
        }
        header p {
            color: #94a3b8;
            font-size: 0.875rem;
        }
        .chat-container {
            flex: 1;
            padding: 1.5rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .message {
            max-width: 80%;
            padding: 0.75rem 1rem;
            border-radius: 0.75rem;
            line-height: 1.5;
            font-size: 0.95rem;
        }
        .bot {
            background-color: #1e293b;
            color: #f1f5f9;
            align-self: flex-start;
            border-bottom-left-radius: 0.1rem;
            border: 1px solid #334155;
        }
        .user {
            background-color: #0284c7;
            color: #ffffff;
            align-self: flex-end;
            border-bottom-right-radius: 0.1rem;
        }
        .input-container {
            padding: 1rem;
            background-color: #1e293b;
            border-top: 1px solid #334155;
            display: flex;
            gap: 0.5rem;
        }
        input {
            flex: 1;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            border: 1px solid #334155;
            background-color: #0f172a;
            color: #ffffff;
            outline: none;
            font-size: 1rem;
        }
        input:focus {
            border-color: #38bdf8;
        }
        button {
            padding: 0.75rem 1.5rem;
            background-color: #0284c7;
            color: white;
            border: none;
            border-radius: 0.5rem;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.2s;
        }
        button:hover {
            background-color: #0369a1;
        }
    </style>
</head>
<body>
    <header>
        <h1>HOPE-IA</h1>
        <p>Tecnologia do Brasil | Sistema Online e Operacional</p>
    </header>

    <div class="chat-container" id="chat">
        <div class="message bot">
            Olá! Sou a <strong>HOPE-IA</strong>. Como posso ajudar-te hoje?
        </div>
    </div>

    <div class="input-container">
        <input type="text" id="userInput" placeholder="Escreve a tua mensagem aqui..." onkeydown="if(event.key === 'Enter') sendMessage()">
        <button onclick="sendMessage()">Enviar</button>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const message = input.value.trim();
            if (!message) return;

            const chat = document.getElementById('chat');

            // Adiciona mensagem do utilizador
            const userDiv = document.createElement('div');
            userDiv.className = 'message user';
            userDiv.textContent = message;
            chat.appendChild(userDiv);

            input.value = '';
            chat.scrollTop = chat.scrollHeight;

            // Faz o envio para a API do Flask
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });

                const data = await response.json();

                const botDiv = document.createElement('div');
                botDiv.className = 'message bot';
                botDiv.textContent = data.response;
                chat.appendChild(botDiv);
            } catch (error) {
                const botDiv = document.createElement('div');
                botDiv.className = 'message bot';
                botDiv.textContent = 'Ocorreu um erro ao processar a mensagem.';
                chat.appendChild(botDiv);
            }

            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_message = data.get('message', '')
    
    # Resposta base da IA
    bot_reply = f"HOPE-IA recebeu: '{user_message}'. O sistema está funcional e pronto para integração!"
    
    return jsonify({'response': bot_reply})

# Bloco essencial para prevenir erro 500 na Vercel:
# Evita que o app.run() bloqueie o servidor serverless da Vercel.
if _name_ == '_main_':
    app.run(debug=True)
