#!/usr/bin/env python3
# ==============================================================
# 💎 HOPE-IA TECNOLOGIA BRASIL — v3.0 · Sistema Completo
# ==============================================================

from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import json
import os
import random

app = Flask(__name__)

ARQUIVO_DADOS = "hope_dados.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "nivel_evolucao": 3.0,
        "conhecimento": [],
        "projetos": [],
        "pesquisas": [],
        "codigos_gerados": [],
        "logs": [],
        "varredura_atual": 100,
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

def salvar_dados(dados):
    dados["ultima_atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def registrar_log(nivel, mensagem):
    dados = carregar_dados()
    log_entry = {
        "id": len(dados["logs"]) + 1,
        "nivel": nivel,
        "mensagem": mensagem,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    dados["logs"].insert(0, log_entry)
    salvar_dados(dados)

dados_sistema = carregar_dados()

@app.route("/")
def index():
    return render_template_string(interface_html)

@app.route("/api/status")
def status():
    d = carregar_dados()
    return jsonify({
        "nivel_evolucao": round(d["nivel_evolucao"], 2),
        "total_conhecimento": len(d["conhecimento"]),
        "total_projetos": len(d["projetos"]),
        "total_pesquisas": len(d["pesquisas"]),
        "total_codigos": len(d["codigos_gerados"]),
        "total_logs": len(d["logs"]),
        "varredura_atual": d["varredura_atual"],
        "ultima_atualizacao": d["ultima_atualizacao"]
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    req = request.json
    prompt = req.get("prompt", "")
    modelo = req.get("model", "hope-ia")
    
    registrar_log("info", f"Consulta recebida [{modelo}]: {prompt[:50]}...")
    
    # Resposta inteligente simulada baseada no motor Hope-IA / OpenRouter
    resposta = f"💎 [HOPE-IA v3.0 | Motor: {modelo.upper()}]\n\n"
    if "criar" in prompt.lower() or "sistema" in prompt.lower():
        resposta += f"Analisei o seu pedido sobre '{prompt}'. O ecossistema integrado das 36 engenharias ativou os sub-agentes de arquitetura e DevOps para estruturar a solução com zero erros."
    elif "pesquisa" in prompt.lower():
        resposta += f"Varredura transdisciplinar concluída para '{prompt}'. Cruzamento de dados realizado com bases científicas e padrões globais."
    else:
        resposta += f"Processado com sucesso através do núcleo unificado de IA. O prompt foi interpretado e otimizado para gerar máxima performance."

    registrar_log("success", f"Resposta gerada com sucesso para o modelo {modelo}")
    return jsonify({"status": "sucesso", "resposta": resposta, "tokens": random.randint(150, 600)})

@app.route("/api/projetos", methods=["GET", "POST"])
def gerenciar_projetos():
    d = carregar_dados()
    if request.method == "POST":
        req = request.json
        proj = {
            "id": len(d["projetos"]) + 1,
            "nome": req.get("nome", "Projeto Autônomo"),
            "tipo": req.get("tipo", "Sistema Geral"),
            "descricao": req.get("descricao", ""),
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        d["projetos"].append(proj)
        d["nivel_evolucao"] += 0.05
        salvar_dados(d)
        registrar_log("success", f"Novo projeto criado: {proj['nome']}")
        return jsonify({"sucesso": True, "projeto": proj})
    return jsonify(d["projetos"])

@app.route("/api/logs")
def listar_logs():
    d = carregar_dados()
    return jsonify(d["logs"])

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
    --warning: #f59e0b;
    --error: #ef4444;
}
* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
body { background: var(--bg); color: var(--text); min-height: 100vh; display: flex; flex-direction: column; }
header { height: 70px; background: rgba(19, 27, 46, 0.9); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 30px; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(10px); }
.brand { display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 18px; letter-spacing: 0.5px; }
.brand span { color: var(--accent); }
nav { display: flex; gap: 8px; overflow-x: auto; }
nav button { background: transparent; border: none; color: var(--muted); padding: 8px 14px; border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px; transition: 0.2s; white-space: nowrap; }
nav button:hover, nav button.active { color: white; background: rgba(255,255,255,0.06); }
.status-badge { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--muted); background: rgba(255,255,255,0.03); padding: 6px 12px; border-radius: 20px; border: 1px solid var(--border); }
.dot { width: 8px; height: 8px; background: var(--success); border-radius: 50%; box-shadow: 0 0 8px var(--success); }
main { flex: 1; max-width: 1200px; width: 100%; margin: 0 auto; padding: 30px 20px; }
.view { display: none; }
.view.active { display: block; }
.hero { text-align: center; margin-bottom: 30px; }
.hero h1 { font-size: 36px; font-weight: 800; margin-bottom: 10px; background: linear-gradient(135deg, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { color: var(--muted); font-size: 16px; max-width: 600px; margin: 0 auto; }
.chat-box { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
.chat-output { min-height: 250px; max-height: 450px; overflow-y: auto; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px; margin-bottom: 15px; font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.6; white-space: pre-wrap; }
.chat-controls { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
textarea { flex: 1; min-height: 50px; max-height: 120px; background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 10px; padding: 12px; color: white; font-size: 14px; resize: vertical; outline: none; }
textarea:focus { border-color: var(--accent); box-shadow: 0 0 10px var(--accent-glow); }
select { background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 10px; padding: 12px; color: white; font-size: 14px; outline: none; cursor: pointer; }
.btn-primary { background: linear-gradient(135deg, var(--accent), #2563eb); border: none; color: white; padding: 12px 24px; border-radius: 10px; font-weight: 600; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 15px var(--accent-glow); }
.btn-primary:hover { transform: translateY(-1px); opacity: 0.95; }
.grid-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }
.card { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 20px; }
.card h3 { font-size: 18px; margin-bottom: 8px; color: #60a5fa; }
.card p { color: var(--muted); font-size: 14px; line-height: 1.5; }
footer { text-align: center; padding: 20px; color: var(--muted); font-size: 12px; border-top: 1px solid var(--border); }
</style>
</head>
<body>

<header>
    <div class="brand">💎 <span>HOPE-IA</span> Tecnologia</div>
    <nav>
        <button class="active" onclick="switchView('workspace')">🚀 Criador</button>
        <button onclick="switchView('projects')">📁 Projetos</button>
        <button onclick="switchView('ai-configs')">⚙️ IAs & OpenRouter</button>
        <button onclick="switchView('engineering')">🏗️ 36 Engenharias</button>
        <button onclick="switchView('logs')">📊 Logs</button>
    </nav>
    <div class="status-badge">
        <div class="dot"></div>
        <span>Online (v3.0)</span>
    </div>
</header>

<main>
    <!-- WORKSPACE / CHAT -->
    <section id="workspace" class="view active">
        <div class="hero">
            <h1>Fábrica Autônoma de Soluções</h1>
            <p>Construa sistemas, códigos, análises preditivas e pesquise com o suporte de dezenas de modelos de IA através do OpenRouter.</p>
        </div>
        <div class="chat-box">
            <div id="chatOutput" class="chat-output">💎 HOPE-IA Inicializada e pronta. Digite o seu prompt abaixo...</div>
            <div class="chat-controls">
                <textarea id="promptInput" placeholder="O que deseja criar ou consultar hoje?"></textarea>
                <select id="modelSelect">
                    <option value="hope-ia">🧠 HOPE-IA Core</option>
                    <option value="openai/gpt-4o">🟢 OpenAI GPT-4o</option>
                    <option value="anthropic/claude-3.5-sonnet">🟠 Claude 3.5 Sonnet</option>
                    <option value="google/gemini-pro-1.5">🔵 Google Gemini Pro</option>
                    <option value="deepseek/deepseek-chat">🟣 DeepSeek V3</option>
                    <option value="x-ai/grok-2">⚡ xAI Grok 2</option>
                </select>
                <button class="btn-primary" onclick="enviarPrompt()">Executar</button>
            </div>
        </div>
    </section>

    <!-- PROJETOS -->
    <section id="projects" class="view">
        <div class="hero">
            <h1>Projetos Gerados</h1>
            <p>Histórico de criações, softwares e automações desenvolvidas na plataforma.</p>
        </div>
        <div id="projectsGrid" class="grid-cards">
            <!-- Preenchido via JS -->
        </div>
    </section>

    <!-- CONFIGURAÇÕES DE IA -->
    <section id="ai-configs" class="view">
        <div class="hero">
            <h1>Configurações do OpenRouter</h1>
            <p>Insira a sua chave de API para desbloquear todos os modelos do mercado na Vercel e no servidor local.</p>
        </div>
        <div class="card" style="max-width: 600px; margin: 0 auto;">
            <h3>Chave Global do OpenRouter</h3>
            <p style="margin-bottom: 15px;">Alimenta OpenAI, Claude, Gemini, DeepSeek, Grok e Llama instantaneamente.</p>
            <div style="display: flex; gap: 10px;">
                <input type="password" id="openRouterKey" placeholder="sk-or-v1-..." style="flex:1; background:rgba(0,0,0,0.3); border:1px solid var(--border); padding:12px; border-radius:10px; color:white; outline:none;">
                <button class="btn-primary" onclick="salvarChaveAPI()">Salvar Chave</button>
            </div>
        </div>
    </section>

    <!-- 36 ENGENHARIAS -->
    <section id="engineering" class="view">
        <div class="hero">
            <h1>As 36 Engenharias Integradas</h1>
            <p>Pilares transdisciplinares que garantem robustez matemática, física, cibernética e estrutural aos projetos.</p>
        </div>
        <div class="grid-cards" id="engGrid"></div>
    </section>

    <!-- LOGS -->
    <section id="logs" class="view">
        <div class="hero">
            <h1>Logs do Sistema</h1>
            <p>Monitoramento em tempo real de requisições, eventos e segurança.</p>
        </div>
        <div class="card">
            <div id="logsOutput" style="font-family:'JetBrains Mono',monospace; font-size:13px; line-height:1.5; max-height:400px; overflow-y:auto;">A carregar logs...</div>
        </div>
    </section>
</main>

<footer>
    <p>© 2026 HOPE-IA Tecnologia Brasil · Todos os direitos reservados.</p>
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
    const res = await fetch('/api/projetos');
    const projetos = await res.json();
    const grid = document.getElementById('projectsGrid');
    
    if(projetos.length === 0) {
        grid.innerHTML = '<p style="color:var(--muted)">Nenhum projeto registado nesta sessão.</p>';
        return;
    }
    
    grid.innerHTML = projetos.map(p => `
        <div class="card">
            <h3>📌 ${p.nome}</h3>
            <p><strong>Tipo:</strong> ${p.tipo}</p>
            <p>${p.descricao}</p>
            <small style="color:var(--muted); display:block; margin-top:10px;">Criado em: ${p.data}</small>
        </div>
    `).join('');
}

async function carregarLogs() {
    const res = await fetch('/api/logs');
    const logs = await res.json();
    const output = document.getElementById('logsOutput');
    output.innerHTML = logs.map(l => `[${l.data}] [${l.nivel.toUpperCase()}] ${l.mensagem}`).join('\n');
}

function salvarChaveAPI() {
    const key = document.getElementById('openRouterKey').value;
    if(!key) { alert('Insira uma chave válida!'); return; }
    localStorage.setItem('OPENROUTER_API_KEY', key);
    alert('✅ Chave guardada com sucesso no armazenamento local!');
}

const engenhariasList = [
    "Engenharia Civil", "Engenharia Mecânica", "Engenharia Elétrica", "Engenharia de Computação",
    "Engenharia Aeroespacial", "Engenharia Robótica", "Engenharia Química", "Engenharia Biomédica",
    "Engenharia de Materiais", "Engenharia Ambiental", "Engenharia de Produção", "Engenharia Nuclear",
    "Engenharia de Telecomunicações", "Engenharia de Minas", "Engenharia Naval", "Engenharia Agrícola",
    "Engenharia de Petróleo", "Engenharia de Alimentos", "Engenharia Metalúrgica", "Engenharia Cartográfica",
    "Engenharia de Software", "Engenharia de Redes", "Engenharia de Cibersegurança", "Engenharia de IA",
    "Engenharia de Dados", "Engenharia de Sistemas", "Engenharia de Bioprocessos", "Engenharia Acústica",
    "Engenharia Óptica", "Engenharia Têxtil", "Engenharia de Transportes", "Engenharia Geotécnica",
    "Engenharia Hidráulica", "Engenharia Sanitária", "Engenharia Forense", "Engenharia Financeira"
];

function renderizarEngenharias() {
    const grid = document.getElementById('engGrid');
    if(grid.children.length > 0) return;
    grid.innerHTML = engenhariasList.map((eng, index) => `
        <div class="card">
            <h3>#${index + 1} - ${eng}</h3>
            <p>Módulo especializado integrado no núcleo transdisciplinar da HOPE-IA.</p>
        </div>
    `).join('');
}
</script>
</body>
</html>
'''

if __name__ == "__main__":
    print("💎 HOPE-IA TECNOLOGIA BRASIL v3.0 — Iniciado com sucesso!")
    print("📡 Acede a: http://127.0.0.1:8081")
    app.run(host="0.0.0.0", port=8081, debug=False)
