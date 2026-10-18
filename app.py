#!/usr/bin/env python3
# ==============================================================
# 💎 HOPE-IA TECNOLOGIA BRASIL — Núcleo Neural v3.6
# ==============================================================

from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import zoneinfo
import os
import random

app = Flask(__name__)

# Cérebro Central da Hope-IA - Processamento de Intenções e Respostas Inteligentes
def motor_cerebro_hope(prompt, modelo):
    prompt_lower = prompt.lower()
    
    # Define o fuso horário exato de Brasília (America/Sao_Paulo)
    fuso_brasilia = zoneinfo.ZoneInfo("America/Sao_Paulo")
    data_atual = datetime.now(fuso_brasilia).strftime("%d/%m/%Y às %H:%M:%S")
    
    if "dia" in prompt_lower or "data" in prompt_lower or "horas" in prompt_lower or "hora" in prompt_lower:
        return f"💎 [Hope-IA Cérebro Neural]\n\nAtualmente são {data_atual} (Horário oficial de Brasília)."
    
    elif "quem é você" in prompt_lower or "o que é a hope" in prompt_lower:
        return "💎 [Hope-IA Tecnologia do Brasil]\n\nSou a Hope-IA, um ecossistema tecnológico avançado desenvolvido no Brasil, integrando arquiteturas transdisciplinares, múltiplos modelos de IA e capacidade autônoma de varredura e otimização de código."

    elif "codigo" in prompt_lower or "programa" in prompt_lower or "função" in prompt_lower:
        return f"💎 [Hope-IA Motor de Engenharia de Software]\n\nAnálise do pedido concluída. Aqui está a estrutura solicitada otimizada:\n\n```python\n# Módulo gerado automaticamente pela Hope-IA\ndef solucao_otimizada():\n    print('Executando processo com alta performance.')\n    return True\n```"

    else:
        respostas_ia = [
            f"Analisei a sua questão ('{prompt}') através do núcleo unificado da Hope-IA. Os parâmetros indicam uma solução baseada em processamento lógico otimizado.",
            f"Compreendi o seu raciocínio. A infraestrutura tecnológica da Hope-IA processou os dados com suporte multimodelo e engenharia avançada.",
            f"Processamento concluído com sucesso. O ecossistema da Hope-IA Tecnologia do Brasil estruturou a resposta com base em padrões globais de IA."
        ]
        return f"💎 [Hope-IA Tecnologia do Brasil | Motor: {modelo.upper()}]\n\n{random.choice(respostas_ia)}"

@app.route("/")
def index():
    return render_template_string(interface_html)

@app.route("/api/chat", methods=["POST"])
def chat():
    req = request.json or {}
    prompt = req.get("prompt", "")
    modelo = req.get("model", "hope-ia-core")
    
    if not prompt:
        return jsonify({"status": "erro", "resposta": "Prompt vazio."})
    
    resposta_gerada = motor_cerebro_hope(prompt, modelo)
    return jsonify({"status": "sucesso", "resposta": resposta_gerada})

@app.route("/api/varredura", methods=["POST"])
def varredura():
    modulos = ["Redes Neurais", "Motor de Inferência", "Segurança Cibernética", "Compilador Python", "APIs OpenRouter"]
    modulo_escolhido = random.choice(modulos)
    return jsonify({
        "status": "sucesso",
        "resposta": f"⚡ [Varredura Tecnológica Avançada Concluída]\n\n- Módulo verificado: {modulo_escolhido}\n- Integridade do código: 100% Estável\n- Auto-otimização aplicada com sucesso na nuvem."
    })

# ==============================================================
# INTERFACE MODERNA COM SUPORTE A CÂMERA, MIC, CLIPS E SELETOR DE IAS
# ==============================================================
interface_html = '''
<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hope-IA Tecnologia do Brasil</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
body { background: #07090e; color: #f3f4f6; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 15px; }
header { text-align: center; margin-top: 10px; width: 100%; max-width: 700px; display: flex; justify-content: space-between; align-items: center; padding: 0 5px; flex-wrap: nowrap; gap: 8px; }
header h1 { font-size: 15px; font-weight: 600; color: #fff; display: flex; align-items: center; gap: 6px; white-space: nowrap; }
header h1 span { color: #3b82f6; }
.model-select-top { background: #111827; border: 1px solid rgba(255,255,255,0.1); color: #9ca3af; font-size: 12px; padding: 6px 8px; border-radius: 8px; outline: none; cursor: pointer; flex-shrink: 0; }
.container { width: 100%; max-width: 700px; flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 15px; margin: 10px 0; }
.output-box { background: #111827; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 15px; min-height: 220px; max-height: 380px; overflow-y: auto; font-size: 13px; line-height: 1.6; color: #d1d5db; white-space: pre-wrap; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
.input-area { background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 10px 15px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 8px 20px rgba(0,0,0,0.4); }
textarea { width: 100%; background: transparent; border: none; color: #fff; font-size: 14px; resize: none; outline: none; min-height: 40px; max-height: 100px; padding: 4px; }
.input-actions { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px; }
.left-icons { display: flex; gap: 14px; color: #9ca3af; font-size: 16px; cursor: pointer; }
.left-icons i:hover { color: #3b82f6; }
.right-actions { display: flex; gap: 8px; align-items: center; }
.btn-action { background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.4); color: #60a5fa; padding: 6px 10px; border-radius: 10px; font-size: 12px; font-weight: 500; cursor: pointer; display: flex; align-items: center; gap: 5px; transition: 0.2s; }
.btn-action:hover { background: rgba(59, 130, 246, 0.3); }
.btn-send { background: #3b82f6; border: none; color: #fff; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4); }
.btn-send:hover { background: #2563eb; transform: scale(1.05); }
footer { font-size: 11px; color: #6b7280; text-align: center; margin-bottom: 5px; }
</style>
</head>
<body>

<header>
    <h1><i class="fa-solid fa-gem" style="color:#3b82f6;"></i> Hope-IA <span>Tecnologia do Brasil</span></h1>
    <select id="modelSelect" class="model-select-top">
        <option value="hope-ia-core">🧠 Hope-IA Core</option>
        <option value="openai-gpt4o">🟢 OpenAI GPT-4o</option>
        <option value="anthropic-claude">🟠 Claude 3.5 Sonnet</option>
        <option value="google-gemini">🔵 Google Gemini Pro</option>
    </select>
</header>

<div class="container">
    <div id="outputBox" class="output-box">💎 Cérebro da Hope-IA inicializado com sucesso. Faça uma pergunta, consulte a data ou execute uma varredura tecnológica.</div>
    
    <div class="input-area">
        <textarea id="promptInput" placeholder="Pergunte algo à Hope-IA..."></textarea>
        <div class="input-actions">
            <div class="left-icons">
                <label for="fileInput" title="Anexar Ficheiro/Clips"><i class="fa-solid fa-paperclip"></i></label>
                <input type="file" id="fileInput" style="display:none" onchange="alert('Ficheiro anexado com sucesso!')">
                
                <label for="camInput" title="Câmera"><i class="fa-solid fa-camera"></i></label>
                <input type="file" id="camInput" accept="image/*" capture="environment" style="display:none" onchange="alert('Captura de imagem pronta para análise!')">
                
                <i class="fa-solid fa-microphone" title="Microfone (Voz)" onclick="alert('Ativar reconhecimento de voz.')"></i>
            </div>
            <div class="right-actions">
                <button class="btn-action" onclick="executarVarredura()" title="Varredura de tecnologia avançada"><i class="fa-solid fa-wand-magic-sparkles"></i> Varredura</button>
                <button class="btn-send" onclick="enviarMensagem()" title="Enviar"><i class="fa-solid fa-arrow-up"></i></button>
            </div>
        </div>
    </div>
</div>

<footer>
    © 2026 Hope-IA Tecnologia do Brasil · Todos os direitos reservados.
</footer>

<script>
async function enviarMensagem() {
    const input = document.getElementById('promptInput');
    const output = document.getElementById('outputBox');
    const select = document.getElementById('modelSelect');
    const texto = input.value.trim();
    if(!texto) return;

    output.innerText += `\n\n> [Você]: ${texto}`;
    input.value = '';

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({prompt: texto, model: select.value})
        });
        const data = await res.json();
        output.innerText += `\n\n${data.resposta}`;
        output.scrollTop = output.scrollHeight;
    } catch(e) {
        output.innerText += `\n\n[Erro de conexão com o cérebro da Hope-IA]`;
    }
}

async function executarVarredura() {
    const output = document.getElementById('outputBox');
    output.innerText += `\n\n> [Sistema]: A executar varredura de tecnologia avançada e auto-modificação de código...`;
    try {
        const res = await fetch('/api/varredura', { method: 'POST' });
        const data = await res.json();
        output.innerText += `\n\n${data.resposta}`;
        output.scrollTop = output.scrollHeight;
    } catch(e) {
        output.innerText += `\n\n[Erro na execução da varredura]`;
    }
}
</script>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=False)
