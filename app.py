#!/usr/bin/env python3
# ==============================================================
# 💎 HOPE-IA TECNOLOGIA DO BRASIL — v4.0 (Sistema Universal)
# ==============================================================

from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import json
import os

app = Flask(_name_)
ARQUIVO_DADOS = "hope_dados.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "nivel_evolucao": 4.5,
        "conhecimento": [],
        "projetos": [],
        "pesquisas": [],
        "codigos_gerados": [],
        "varreduras": [],
        "imagens_geradas": [],
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

def salvar_dados(dados):
    dados["ultima_atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

dados_sistema = carregar_dados()

@app.route("/")
def index():
    return render_template_string(interface_html)

@app.route("/status")
def status():
    return jsonify({
        "nivel_evolucao": round(dados_sistema["nivel_evolucao"], 2),
        "total_conhecimento": len(dados_sistema["conhecimento"]),
        "total_projetos": len(dados_sistema["projetos"]),
        "total_pesquisas": len(dados_sistema["pesquisas"]),
        "total_codigos": len(dados_sistema["codigos_gerados"]),
        "total_varreduras": len(dados_sistema["varreduras"]),
        "ultima_atualizacao": dados_sistema["ultima_atualizacao"]
    })

@app.route("/processar", methods=["POST"])
def processar():
    dados = request.json
    modo = dados.get("modo", "chat")
    entrada = dados.get("entrada", "").strip()
    
    resposta = ""
    if modo == "chat":
        resposta = f"💎 [NÚCLEO UNIVERSAL] Processamento inteligente concluído para: '{entrada}'. A HOPE-IA cruzou dados de texto, código e lógica neural com sucesso."
    elif modo == "pesquisa":
        resposta = f"🌐 [VARREDURA GLOBAL] Dados indexados e coletados com sucesso sobre: '{entrada}'. Fontes públicas e padrões tecnológicos mapeados."
    elif modo == "imagem":
        dados_sistema["imagens_geradas"].append({"prompt": entrada, "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        resposta = f"🎨 [GERADOR VISUAL] Imagem fotorrealista e conceitual gerada com sucesso para o prompt: '{entrada}'."
    elif modo == "codigo":
        dados_sistema["codigos_gerados"].append({"titulo": entrada, "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
        resposta = f"💻 [MOTOR DE CÓDIGO] Estrutura gerada e otimizada para: '{entrada}'."
    
    dados_sistema["nivel_evolucao"] += 0.03
    salvar_dados(dados_sistema)
    
    return jsonify({
        "sucesso": True,
        "resposta": resposta,
        "nivel": round(dados_sistema["nivel_evolucao"], 2)
    })

@app.route("/varrer", methods=["POST"])
def varrer():
    dados = request.json
    termo = dados.get("termo", "Tecnologia Brasil")
    reg = {
        "id": len(dados_sistema["varreduras"]) + 1,
        "termo": termo,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    dados_sistema["varreduras"].append(reg)
    dados_sistema["nivel_evolucao"] += 0.05
    salvar_dados(dados_sistema)
    return jsonify({
        "sucesso": True,
        "mensagem": f"🔍 Varredura executada via Bola Azul para o termo: '{termo}'",
        "nivel": round(dados_sistema["nivel_evolucao"], 2)
    })

interface_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOPE-IA — Tecnologia Brasil</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Roboto, sans-serif; }
        body {
            background: linear-gradient(180deg, #dfcbfd 0%, #f4ebff 50%, #ffffff 100%);
            color: #2e1065;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-bottom: 90px;
        }
        .topo {
            width: 100%;
            max-width: 480px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 20px;
        }
        .logo-container {
            display: flex;
            align-items: center;
            gap: 10px;
            background: #7c3aed;
            padding: 6px 14px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            font-size: 15px;
            box-shadow: 0 4px 12px rgba(124,58,237,0.3);
        }
        .logo-icone { background: #5b21b6; width: 24px; height: 24px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 12px; }
        .tres-pontos { font-size: 20px; cursor: pointer; color: #4c1d95; }

        .cabecalho-texto {
            text-align: center;
            margin-top: 10px;
            margin-bottom: 15px;
        }
        .cabecalho-texto h1 {
            font-size: 34px;
            font-weight: 800;
            color: #3b0764;
            letter-spacing: -0.5px;
        }
        .cabecalho-texto p {
            font-size: 15px;
            color: #6b21a8;
            font-weight: 500;
        }

        .nuvem-card {
            width: 90%;
            max-width: 420px;
            background: radial-gradient(circle, rgba(243,232,255,0.8) 0%, rgba(221,214,254,0.4) 100%);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(216, 180, 254, 0.6);
            border-radius: 28px;
            padding: 24px 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(124, 58, 237, 0.15);
            margin-bottom: 15px;
        }
        .nuvem-icone {
            width: 100px;
            height: 80px;
            margin: 0 auto 10px auto;
            background: radial-gradient(circle, #fbcfe8 0%, #c084fc 60%, #7c3aed 100%);
            border-radius: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 25px rgba(192, 132, 252, 0.8);
            animation: flutuar 3s ease-in-out infinite;
        }
        @keyframes flutuar { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
        .cerebro { font-size: 36px; filter: drop-shadow(0 0 8px white); }

        .modo-seletor {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin-bottom: 12px;
            width: 90%;
            max-width: 420px;
            flex-wrap: wrap;
        }
        .btn-modo {
            background: rgba(255,255,255,0.7);
            border: 1px solid #d8b4fe;
            padding: 6px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            color: #5b21b6;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn-modo.ativo {
            background: #7c3aed;
            color: white;
            border-color: #7c3aed;
        }

        .barra-pesquisa {
            width: 90%;
            max-width: 420px;
            display: flex;
            align-items: center;
            background: white;
            border-radius: 30px;
            padding: 6px 16px;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.12);
            margin-bottom: 15px;
            border: 1px solid #e9d5ff;
        }
        .barra-pesquisa input {
            flex: 1;
            border: none;
            outline: none;
            font-size: 14px;
            padding: 10px;
            color: #3b0764;
            background: transparent;
        }
        .lupa-btn {
            background: none;
            border: none;
            font-size: 18px;
            cursor: pointer;
            color: #7c3aed;
            padding: 4px;
        }
        .btn-enviar-pesquisa {
            background: #7c3aed;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(124,58,237,0.3);
            transition: 0.2s;
        }

        .resposta-card {
            width: 90%;
            max-width: 420px;
            background: white;
            border-radius: 20px;
            padding: 16px 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(124,58,237,0.08);
            border-left: 4px solid #7c3aed;
            display: none;
        }
        .resposta-card h3 { font-size: 14px; color: #7c3aed; margin-bottom: 6px; }
        .resposta-card p { font-size: 14px; color: #374151; line-height: 1.5; }

        .card-acao {
            width: 90%;
            max-width: 420px;
            background: white;
            border-radius: 24px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.08);
            margin-bottom: 20px;
            border: 1px solid #f3e8ff;
        }
        .mic-container { display: flex; align-items: center; gap: 12px; }
        .mic-bola {
            width: 42px; height: 42px;
            background: #d8b4fe;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 18px; color: #5b21b6; cursor: pointer;
        }
        .acoes-direita { display: flex; align-items: center; gap: 10px; }
        .circulo-camera, .circulo-seta {
            width: 42px; height: 42px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; border: none; font-size: 18px;
        }
        .circulo-camera { background: #f3e8ff; color: #7c3aed; }
        .circulo-seta { background: #7c3aed; color: white; box-shadow: 0 4px 10px rgba(124,58,237,0.3); }

        .bola-azul-varredura {
            position: fixed;
            bottom: 85px; right: 20px;
            width: 62px; height: 62px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            border-radius: 50%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            color: white;
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
            cursor: pointer; z-index: 1000;
            border: 3px solid white;
            animation: pulsarBola 2s infinite;
        }
        .bola-azul-varredura span { font-size: 10px; font-weight: bold; margin-top: -2px; }
        @keyframes pulsarBola {
            0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.6); }
            50% { transform: scale(1.08); box-shadow: 0 0 0 12px rgba(59, 130, 246, 0); }
        }

        .modal-varredura {
            display: none;
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.5); backdrop-filter: blur(5px);
            z-index: 2000; justify-content: center; align-items: center; padding: 20px;
        }
        .modal-conteudo {
            background: white; width: 100%; max-width: 400px;
            border-radius: 24px; padding: 24px; position: relative;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .fechar-modal {
            position: absolute; top: 16px; right: 20px;
            background: none; border: none; font-size: 20px; cursor: pointer; color: #6b7280;
        }

        .nav-inferior {
            position: fixed; bottom: 0; left: 0; width: 100%;
            background: rgba(59, 7, 100, 0.96); backdrop-filter: blur(10px);
            display: flex; justify-content: space-around; padding: 12px 10px;
            border-top-left-radius: 20px; border-top-right-radius: 20px;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.15); z-index: 900;
        }
        .nav-item {
            background: none; border: none; color: #d8b4fe; font-size: 13px;
            display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer;
        }
        .nav-item.ativo { color: white; font-weight: bold; }
        .nav-item span { font-size: 18px; }
    </style>
</head>
<body>

    <div class="topo">
        <div class="logo-container">
            <div class="logo-icone">💎</div>
            HOPE-IA
        </div>
        <div class="tres-pontos" onclick="alert('💎 HOPE-IA Universal — v4.0 Ativada.')">⋮</div>
    </div>

    <div class="cabecalho-texto">
        <h1>HOPE-IA</h1>
        <p>Tecnologia Brasil</p>
    </div>

    <div class="nuvem-card">
        <div class="nuvem-icone">
            <div class="cerebro">🧠</div>
        </div>
        <p style="font-size: 13px; color: #6b21a8; font-weight: 500;">Núcleo Universal Ativo • Nível <span id="txt-nivel">4.5</span></p>
    </div>

    <div class="modo-seletor">
        <button class="btn-modo ativo" id="m-chat" onclick="mudarModo('chat')">💬 Chat</button>
        <button class="btn-modo" id="m-pesquisa" onclick="mudarModo('pesquisa')">🌐 Pesquisa</button>
        <button class="btn-modo" id="m-imagem" onclick="mudarModo('imagem')">🎨 Imagem</button>
        <button class="btn-modo" id="m-codigo" onclick="mudarModo('codigo')">💻 Código</button>
    </div>

    <div class="barra-pesquisa">
        <button class="lupa-btn" onclick="executarAcao()">🔍</button>
        <input type="text" id="input-pergunta" placeholder="Pergunte à HOPE-IA..." onkeypress="if(event.key === 'Enter') executarAcao()">
        <button class="btn-enviar-pesquisa" onclick="executarAcao()">Sends</button>
    </div>

    <div class="resposta-card" id="card-resposta">
        <h3>✨ Resposta da HOPE-IA:</h3>
        <p id="texto-resposta">Aguardando comando...</p>
    </div>

    <div class="card-acao">
        <div class="mic-container">
            <div class="mic-bola" onclick="alert('🎤 Reconhecimento de voz ativado.')">🎤</div>
            <span style="font-size: 14px; color: #6b21a8; font-weight: 500;">à HOPE-IA...</span>
        </div>
        <div class="acoes-direita">
            <button class="circulo-camera" onclick="alert('📸 Visão computacional e OCR ativados.')">📷</button>
            <button class="circulo-seta" onclick="executarAcao()">➔</button>
        </div>
    </div>

    <div class="bola-azul-varredura" onclick="abrirVarredura()" title="Varredura Global">
        <span style="font-size: 20px;">🌐</span>
        <span>Varredura</span>
    </div>

    <div class="modal-varredura" id="modal-varredura">
        <div class="modal-conteudo">
            <button class="fechar-modal" onclick="fecharVarredura()">✕</button>
            <h2 style="color: #1d4ed8; margin-bottom: 12px; font-size: 18px;">🌐 Varredura Global Ativa</h2>
            <p style="font-size: 13px; color: #4b5563; margin-bottom: 16px;">
                Pesquise e indexe dados abertos em tempo real.
            </p>
            <input type="text" id="input-termo-varredura" placeholder="Tema para varrer..." style="width: 100%; padding: 12px; border-radius: 12px; border: 2px solid #93c5fd; outline: none; margin-bottom: 12px; font-size: 14px;">
            <button onclick="realizarVarredura()" style="width: 100%; background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; border: none; padding: 12px; border-radius: 12px; font-weight: bold; cursor: pointer;">
                🚀 Executar Varredura
            </button>
            <div id="res-varredura" style="margin-top: 15px; font-size: 13px; color: #1e3a8a; background: #eff6ff; padding: 10px; border-radius: 8px; display: none;"></div>
        </div>
    </div>

    <div class="nav-inferior">
        <button class="nav-item ativo" onclick="mudarNav(this)"><span>🏠</span> Início</button>
        <button class="nav-item" onclick="mudarNav(this); abrirVarredura();"><span>☁️</span> Nuvens</button>
        <button class="nav-item" onclick="mudarNav(this); alert('⚙️ Configurações ativadas.');"><span>⚙️</span> Configurações</button>
        <button class="nav-item" onclick="mudarNav(this); alert('💎 Bola AI — Ativada.');"><span>💎</span> Bola AI</button>
    </div>

    <script>
        let modoAtual = 'chat';

        function mudarModo(m) {
            document.querySelectorAll('.btn-modo').forEach(b => b.classList.remove('ativo'));
            document.getElementById('m-' + m).classList.add('ativo');
            modoAtual = m;
            const input = document.getElementById('input-pergunta');
            if (m === 'chat') input.placeholder = 'Pergunte à HOPE-IA...';
            if (m === 'pesquisa') input.placeholder = 'Pesquise na web global...';
            if (m === 'imagem') input.placeholder = 'Descreva a imagem para gerar...';
            if (m === 'codigo') input.placeholder = 'Descreva o código ou algoritmo...';
        }

        async function executarAcao() {
            const input = document.getElementById('input-pergunta');
            const val = input.value.trim();
            if (!val) return;

            const card = document.getElementById('card-resposta');
            const txt = document.getElementById('texto-resposta');
            card.style.display = 'block';
            txt.innerHTML = '💎 Processando núcleo universal...';

            try {
                const res = await fetch('/processar', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({modo: modoAtual, entrada: val})
                });
                const d = await res.json();
                txt.innerHTML = d.resposta;
                document.getElementById('txt-nivel').textContent = d.nivel
