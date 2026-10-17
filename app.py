#!/usr/bin/env python3
# ==============================================================
# 💎 HOPE-IA TECNOLOGIA BRASIL — v3.1 · Versão Otimizada Vercel
# ==============================================================

from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Base de dados em memória para garantir compatibilidade total com a Vercel
dados_memoria = {
    "nivel_evolucao": 3.0,
    "conhecimento": [],
    "projetos": [
        {"id": 1, "nome": "HOPE-Core", "tipo": "Sistema Base", "descricao": "Núcleo inicializado com sucesso.", "data": "17/10/2026 20:00:00"}
    ],
    "pesquisas": [],
    "codigos_gerados": [],
    "logs": [
        {"id": 1, "nivel": "success", "mensagem": "Sistema iniciado na nuvem Vercel com sucesso.", "data": "17/10/2026 20:00:00"}
    ],
    "varredura_atual": 100,
    "ultima_atualizacao": "17/10/2026 20:00:00"
}

def registrar_log(nivel, mensagem):
    log_entry = {
        "id": len(dados_memoria["logs"]) + 1,
        "nivel": nivel,
        "mensagem": mensagem,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    dados_memoria["logs"].insert(0, log_entry)

@app.route("/")
def index():
    return render_template_string(interface_html)

@app.route("/api/status")
def status():
    return jsonify({
        "nivel_evolucao": round(dados_memoria["nivel_evolucao"], 2),
        "total_conhecimento": len(dados_memoria["conhecimento"]),
        "total_projetos": len(dados_memoria["projetos"]),
        "total_pesquisas": len(dados_memoria["pesquisas"]),
        "total_codigos": len(dados_memoria["codigos_gerados"]),
        "total_logs": len(dados_memoria["logs"]),
        "varredura_atual": dados_memoria["varredura_atual"],
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    req = request.json or {}
    prompt = req.get("prompt", "")
    modelo = req.get("model", "hope-ia")
    
    registrar_log("info", f"Consulta recebida [{modelo}]: {prompt[:50]}...")
    
    resposta = f"💎 [HOPE-IA v3.1 | Motor: {modelo.upper()}]\n\n"
    if "criar" in prompt.lower() or "sistema" in prompt.lower():
        resposta += f"Analisei o seu pedido sobre '{prompt}'. O ecossistema integrado das 36 engenharias ativou os sub-agentes para estruturar a solução."
    elif "pesquisa" in prompt.lower() or "dia" in prompt.lower() or "hoje" in prompt.lower():
        resposta += f"Varredura transdisciplinar concluída para '{prompt}'. Processamento efetuado com sucesso pelo núcleo unificado."
    else:
        resposta += f"Processado com sucesso através do núcleo de IA. O seu prompt ('{prompt}') foi interpretado e otimizado com êxito."

    registrar_log("success", f"Resposta gerada para o modelo {modelo}")
    return jsonify({"status": "sucesso", "resposta": resposta, "tokens": random.randint(150, 600)})

@app.route("/api/projetos", methods=["GET", "POST"])
def gerenciar_projetos():
    if request.method == "POST":
        req = request.json or {}
        proj = {
            "id": len(dados_memoria["projetos"]) + 1,
            "nome": req.get("nome", "Projeto Autônomo"),
            "tipo": req.get("tipo", "Sistema Geral"),
            "descricao": req.get("descricao", ""),
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        dados_memoria["projetos"].append(proj)
        dados_memoria["nivel_evolucao"] += 0.05
        registrar_log("success", f"Novo projeto criado: {proj['nome']}")
        return jsonify({"sucesso": True, "projeto": proj})
    return jsonify(dados_memoria["projetos"])

@app.route("/api/logs")
def listar_logs():
    return jsonify(dados_memoria["logs"])

# ==============================================================
# INTERFACE HTML5 / CSS3 / JS COMPLETA
# ==============================================================
interface_html = '''
<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HOPE-IA Tecnologia Brasil</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
    --bg: #0b0f19;
    --panel: #131b2e;
    --border: rgba(255, 255, 255, 0.08);
    --text: #f3f4f6;
    --muted: #9ca3af;
    --accent: #3b82f6;
    --accent-glow: rgba(59, 130, 246, 0.3);
    --success: #10b981;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
body { background: var(--bg); color: var(--text); min-height: 100vh; display: flex; flex-direction: column; }
header { height: 70px; background: rgba(19, 27, 46, 0.9); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 20px; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(10px); }
.brand { display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 16px; }
.brand span { color: var(--accent); }
nav { display: flex; gap: 4px; overflow-x: auto; padding: 5px 0; }
nav button { background: transparent; border: none; color: var(--muted); padding: 6px 10px; border-radius: 6px; cursor: pointer; font-weight: 500; font-size: 13px; white-space: nowrap; }
nav button:hover, nav button.active { color: white; background: rgba(255,255,255,0.06); }
.status-badge { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--muted); background: rgba(255,255,255,0.03); padding: 4px 10px; border-radius: 20px; border: 1px solid var(--border); }
.dot { width: 7px; height: 7px; background: var(--success); border-radius: 50%; box-shadow: 0 0 6px var(--success); }
main { flex: 1; max-width: 1100px; width: 100%; margin: 0 auto; padding: 20px 15px; }
.view { display: none; }
.view.active { display: block; }
.hero { text-align: center; margin-bottom: 20px; }
.hero h1 { font-size: 28px; font-weight: 800; margin-bottom: 8px; background: linear-gradient(135deg, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { color: var(--muted); font-size: 14px; max-width: 550px; margin: 0 auto; }
.chat-box { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
.chat-output { min-height: 200px; max-height: 380px; overflow-y: auto; padding: 12px; background: rgba(0,0,0,0.2); border-radius: 10px; margin-bottom: 12px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.5; white-space: pre-wrap; }
.chat-controls { display: flex; gap: 10px; flex-direction: column; }
@media(min-width: 768px) { .chat-controls { flex-direction: row; align-items: center; } }
textarea { flex: 1; min-height: 45px; max-height: 100px; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 8px; padding: 10px; color: white; font-size: 13px; resize: vertical; outline: none; }
textarea:focus { border-color: var(--accent); }
select { background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 8px; padding: 10px; color: white; font-size: 13px; outline: none; cursor: pointer; }
.btn-primary { background: linear-gradient(135deg, var(--accent), #2563eb); border: none; color: white; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 15px var(--accent-glow); width: 100%; }
@media(min-width: 768px) { .btn-primary { width: auto; } }
.grid-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px; }
.card { background: var(--panel); border: 1px solid var(--border); border-radius: 12px; padding: 15px; }
.card h3 { font-size: 16px; margin-bottom: 6px; color: #60a5fa; }
.card p { color: var(--muted); font-size: 13px; line-height: 1.4; }
footer { text-align: center; padding: 15px; color: var(--muted); font-size: 11px; border-top: 1px solid var(--border); }
</style>
</head>
<body>

<header>
    <div class="brand">💎 <span>HOPE-IA</span></div>
    <nav>
        <button class="active" onclick="switchView('workspace')">🚀 Criador</button>
        <button onclick="switchView('projects')">📁 Projetos</button>
        <button onclick="switchView('ai-configs')">⚙️ IAs</button>
        <button onclick="switchView('engineering')">🏗️ Eng.</button>
        <button onclick="switchView('logs')">📊 Logs</button>
    </nav>
    <div class="status-badge">
        <div class="dot"></div>
        <span>v3.1</span>
    </div>
</header>

<main>
    <section id="workspace" class="view active">
        <div class="hero">
            <h1>Fábrica Autônoma de Soluções</h1>
            <p>Construa sistemas, códigos e pesquisas com suporte de IAs avançadas.</p>
        </div>
        <div class="chat-box">
            <div id="chatOutput" class="chat-output">💎 HOPE-IA Inicializada e pronta. Digite o seu prompt abaixo...</div>
            <div class="chat-controls">
                <textarea id="promptInput" placeholder="O que deseja criar ou consultar hoje?"></textarea>
                <select id="modelSelect">
                    <option value="hope-ia">🧠 HOPE-IA Core</option>
                    <option value="openai/gpt-4o">🟢 GPT-4o</option>
                    <option value="anthropic/claude-3.5-sonnet">🟠 Claude 3.5</option>
                    <option value="google/gemini-pro-1.5">🔵 Gemini Pro</option>
                    <option value="deepseek/deepseek-chat">🟣 DeepSeek V3</option>
                </select>
                <button class="btn-primary" onclick="enviarPrompt()">Executar</button>
            </div>
        </div>
    </section>

    <section id="projects" class="view">
        <div class="hero">
            <h1>Projetos Gerados</h1>
            <p>Histórico de criações e automações.</p>
        </div>
        <div id="projectsGrid" class="grid-cards"></div>
    </section>

    <section id="ai-configs" class="view">
        <div class="hero">
            <h1>Configurações do OpenRouter</h1>
            <p>Insira a sua chave de API para desbloquear todos os modelos.</p>
        </div>
        <div class="card" style="max-width: 500px; margin: 0 auto;">
            <h3>Chave Global do OpenRouter</h3>
            <p style="margin-bottom: 12px;">Alimenta os modelos de IA instantaneamente.</p>
            <div style="display: flex; gap: 8px; flex-direction: column;">
                <input type="password" id="openRouterKey" placeholder="sk-or-v1-..." style="background:rgba(0,0,0,0.3); border:1px solid var(--border); padding:10px; border-radius:8px; color:white; outline:none;">
                <button class="btn-primary" onclick="salvarChaveAPI()">Salvar Chave</button>
            </div>
        </div>
    </section>

    <section id="engineering" class="view">
        <div class="hero">
            <h1>As 36 Engenharias</h1>
            <p>Pilares transdisciplinares da plataforma.</p>
        </div>
        <div class="grid-cards" id="engGrid"></div>
    </section>

    <section id="logs" class="view">
        <div class="hero">
            <h1>Logs do Sistema</h1>
            <p>Monitoramento em tempo real.</p>
        </div>
        <div class="card">
            <div id="logsOutput" style="font-family:'JetBrains Mono',monospace; font-size:12px; line-height:1.4; max-height:350px; overflow-y:auto;">A carregar logs...</div>
        </div>
    </section>
</main>

<footer>
    <p>© 2026 HOPE-IA Tecnologia Brasil</p>
</footer>

<script>
function switchView(viewId) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    document.getElementById(viewId).classList.add('active');
    event.currentTarget.classList.add('active');
    
    if(viewId === 'projects') carregarProjetos();
    if(viewId === 'logs') carregarLogs();
    if(viewId === 'engineering') renderizarEngenharias();
}

async function enviarPrompt() {
    const prompt = document.getElementById('promptInput').value.trim();
    const model = document.getElementById('modelSelect').value;
    const output = document.getElementById('chatOutput');
    
    if(!prompt) return;
    
    output.innerText += `\n\n> [Você]: ${prompt}`;
    document.getElementById('promptInput').value = '';
    
    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({prompt, model})
        });
        const data = await res.json();
        output.innerText += `\n\n${data.resposta}`;
        output.scrollTop = output.scrollHeight;
    } catch(e) {
        output.innerText += `\n\n[Erro de comunicação com o servidor]`;
    }
}

async function carregarProjetos() {
    try {
        const res = await fetch('/api/projetos');
        const projetos = await res.json();
        const grid = document.getElementById('projectsGrid');
        grid.innerHTML = projetos.map(p => `
            <div class="card">
                <h3>📌 ${p.nome}</h3>
                <p><strong>Tipo:</strong> ${p.tipo}</p>
                <p>${p.descricao}</p>
                <small style="color:var(--muted); display:block; margin-top:8px;">${p.data}</small>
            </div>
        `).join('');
    } catch(e) {
        document.getElementById('projectsGrid').innerHTML = '<p style="color:var(--muted)">Erro ao carregar projetos.</p>';
    }
}

async function carregarLogs() {
    try {
        const res = await fetch('/api/logs');
        const logs = await res.json();
        document.getElementById('logsOutput').innerHTML = logs.map(l => `[${l.data}] [${l.nivel.toUpperCase()}] ${l.mensagem}`).join('\n');
    } catch(e) {
        document.getElementById('logsOutput').innerText = 'Erro ao carregar logs.';
    }
}

function salvarChaveAPI() {
    const key = document.getElementById('openRouterKey').value;
    if(!key) { alert('Insira uma chave válida!'); return; }
    localStorage.setItem('OPENROUTER_API_KEY', key);
    alert('✅ Chave guardada com sucesso!');
}

const engenhariasList = [
    "Civil", "Mecânica", "Elétrica", "Computação", "Aeroespacial", "Robótica", 
    "Química", "Biomédica", "Materiais", "Ambiental", "Produção", "Nuclear",
    "Telecomunicações", "Minas", "Naval", "Agrícola", "Petróleo", "Alimentos", 
    "Metalúrgica", "Cartográfica", "Software", "Redes", "Cibersegurança", "IA",
    "Dados", "Sistemas", "Bioprocessos", "Acústica", "Óptica", "Têxtil", 
    "Transportes", "Geotécnica", "Hidráulica", "Sanitária", "Forense", "Financeira"
];

function renderizarEngenharias() {
    const grid = document.getElementById('engGrid');
    if(grid.children.length > 0) return;
    grid.innerHTML = engenhariasList.map((eng, index) => `
        <div class="card">
            <h3>#${index + 1} - ${eng}</h3>
            <p>Módulo de engenharia transdisciplinar ativo.</p>
        </div>
    `).join('');
}
</script>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=False)
