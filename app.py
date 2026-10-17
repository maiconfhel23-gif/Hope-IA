#!/usr/bin/env python3
from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(interface_html)

@app.route("/api/chat", methods=["POST"])
def chat():
    req = request.json or {}
    prompt = req.get("prompt", "")
    return jsonify({
        "status": "sucesso",
        "resposta": f"💎 [Hope IA - Tecnologia do Brasil]\n\nComando processado com sucesso: '{prompt}'. Sistemas ativados com alta performance."
    })

@app.route("/api/varredura", methods=["POST"])
def varredura():
    return jsonify({
        "status": "sucesso",
        "resposta": "⚡ Varredura de tecnologia avançada concluída! Módulos otimizados e prontos."
    })

interface_html = '''
<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hope IA - Tecnologia do Brasil</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
body { background: #07090e; color: #f3f4f6; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 20px; }
header { text-align: center; margin-top: 20px; }
header h1 { font-size: 22px; font-weight: 600; color: #fff; display: flex; align-items: center; justify-content: center; gap: 8px; }
header h1 span { color: #3b82f6; }
.container { width: 100%; max-width: 650px; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 20px; }
.output-box { background: #111827; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; min-height: 200px; max-height: 350px; overflow-y: auto; font-size: 14px; line-height: 1.6; color: #9ca3af; white-space: pre-wrap; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
.input-area { background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 10px 15px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.4); }
textarea { width: 100%; background: transparent; border: none; color: #fff; font-size: 15px; resize: none; outline: none; min-height: 45px; max-height: 120px; padding: 5px; }
.input-actions { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px; }
.left-icons { display: flex; gap: 15px; color: #9ca3af; font-size: 18px; cursor: pointer; }
.left-icons i:hover { color: #3b82f6; }
.right-actions { display: flex; gap: 10px; align-items: center; }
.btn-action { background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.4); color: #60a5fa; padding: 8px 12px; border-radius: 12px; font-size: 13px; font-weight: 500; cursor: pointer; display: flex; align-items: center; gap: 6px; transition: 0.2s; }
.btn-action:hover { background: rgba(59, 130, 246, 0.3); }
.btn-send { background: #3b82f6; border: none; color: #fff; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4); }
.btn-send:hover { background: #2563eb; transform: scale(1.05); }
footer { font-size: 11px; color: #6b7280; text-align: center; margin-bottom: 10px; }
</style>
</head>
<body>

<header>
    <h1><i class="fa-solid fa-gem" style="color:#3b82f6;"></i> Hope IA <span>Tecnologia do Brasil</span></h1>
</header>

<div class="container">
    <div id="outputBox" class="output-box">💎 Hope IA inicializada. Como posso ajudar na tecnologia de hoje?</div>
    
    <div class="input-area">
        <textarea id="promptInput" placeholder="Mensagem para Hope IA..."></textarea>
        <div class="input-actions">
            <div class="left-icons">
                <i class="fa-solid fa-paperclip" title="Anexar Ficheiro/Clips" onclick="alert('Funcionalidade de anexo pronta.')"></i>
                <i class="fa-solid fa-camera" title="Câmera" onclick="alert('Ativar câmara.')"></i>
                <i class="fa-solid fa-microphone" title="Microfone" onclick="alert('Ativar microfone (Voz).')"></i>
            </div>
            <div class="right-actions">
                <button class="btn-action" onclick="executarVarredura()" title="Varredura de tecnologia avançada"><i class="fa-solid fa-wand-magic-sparkles"></i> Varredura</button>
                <button class="btn-send" onclick="enviarMensagem()" title="Enviar"><i class="fa-solid fa-arrow-up"></i></button>
            </div>
        </div>
    </div>
</div>

<footer>
    © 2026 Hope IA · Todos os direitos reservados.
</footer>

<script>
async function enviarMensagem() {
    const input = document.getElementById('promptInput');
    const output = document.getElementById('outputBox');
    const texto = input.value.trim();
    if(!texto) return;

    output.innerText += `\\n\\n> ${texto}`;
    input.value = '';

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({prompt: texto})
        });
        const data = await res.json();
        output.innerText += `\\n\\n${data.resposta}`;
        output.scrollTop = output.scrollHeight;
    } catch(e) {
        output.innerText += `\\n\\n[Erro de conexão]`;
    }
}

async function executarVarredura() {
    const output = document.getElementById('outputBox');
    output.innerText += `\\n\\n> [Sistema]: A executar varredura de tecnologia avançada e otimização de código...`;
    try {
        const res = await fetch('/api/varredura', { method: 'POST' });
        const data = await res.json();
        output.innerText += `\\n\\n${data.resposta}`;
        output.scrollTop = output.scrollHeight;
    } catch(e) {
        output.innerText += `\\n\\n[Erro na varredura]`;
    }
}
</script>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=False)
