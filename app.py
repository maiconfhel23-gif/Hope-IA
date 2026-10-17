import json
import os
import time
import urllib.error
import urllib.request

from flask import Flask, Response, jsonify, request

app = Flask(_name_)

OPENROUTER = "https://openrouter.ai/api/v1"
FORNECEDORES = {
    "openai": "OpenAI",
    "anthropic": "Anthropic (Claude)",
    "google": "Google (Gemini)",
    "x-ai": "xAI (Grok)",
    "deepseek": "DeepSeek",
    "moonshotai": "Kimi (Moonshot)",
    "mistralai": "Mistral",
    "meta-llama": "Meta (Llama)",
    "qwen": "Qwen",
    "perplexity": "Perplexity",
    "cohere": "Cohere",
}
SISTEMA = (
    "Você é a Hope-IA, assistente da HOPE-IA Tecnologia Brasil. "
    "Responda em português do Brasil, de forma clara e direta."
)
_cache = {"hora": 0, "lista": []}


def pedir(url, corpo=None, chave=None, tempo=50):
    cabecalhos = {"Content-Type": "application/json", "X-Title": "HOPE-IA"}
    if chave:
        cabecalhos["Authorization"] = "Bearer " + chave
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(url, data=dados, headers=cabecalhos)
    with urllib.request.urlopen(req, timeout=tempo) as r:
        return json.loads(r.read().decode())


INTERFACE_HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>HOPE-IA Tecnologia Brasil</title>
<style>
  :root { --topo:#e9defa; --meio:#c9b3f2; --roxo:#6a3fc8; --escuro:#3b1f7a; --branco:#fff; --vidro:rgba(255,255,255,.72); }
  * { box-sizing:border-box; margin:0; padding:0; -webkit-tap-highlight-color:transparent; }
  html, body { height:100%; }
  body { font-family:"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif; color:var(--escuro);
    background:linear-gradient(170deg,var(--topo) 0%,var(--meio) 100%); display:flex; flex-direction:column; align-items:center;
    padding:env(safe-area-inset-top) 18px calc(env(safe-area-inset-bottom) + 12px); overflow-x:hidden; }
  .logo { margin-top:18px; font-weight:800; letter-spacing:.04em; font-size:1.05rem; color:var(--roxo); }
  main { flex:1; width:100%; max-width:560px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:6px; }
  h1 { font-size:clamp(2.6rem,13vw,4rem); line-height:1; font-weight:800; letter-spacing:-.02em; }
  .sub { font-size:1.15rem; font-weight:500; opacity:.8; }
  .cerebro { width:min(62vw,250px); margin:18px 0 8px; animation:flutuar 5s ease-in-out infinite; filter:drop-shadow(0 14px 22px rgba(106,63,200,.28)); }
  @keyframes flutuar { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-9px); } }
  @media (prefers-reduced-motion:reduce) { .cerebro { animation:none; } }
  body.conversando main { display:none; }
  #conversa { width:100%; max-width:560px; flex:1; overflow-y:auto; display:none; flex-direction:column; gap:8px; margin:12px 0; text-align:left; }
  body.conversando #conversa { display:flex; }
  .msg { padding:10px 14px; border-radius:16px; max-width:90%; font-size:.97rem; line-height:1.45; white-space:pre-wrap; word-wrap:break-word; }
  .msg.eu { align-self:flex-end; background:var(--roxo); color:var(--branco); border-bottom-right-radius:4px; }
  .msg.ia { align-self:flex-start; background:var(--vidro); border-bottom-left-radius:4px; }
  .seletor { width:100%; max-width:560px; margin-bottom:8px; }
  .seletor select { width:100%; border:0; border-radius:999px; padding:11px 16px; font-size:.95rem; font-weight:600; color:var(--escuro);
    background:var(--vidro); box-shadow:0 4px 14px rgba(59,31,122,.12); outline:0; }
  .busca { width:100%; max-width:560px; display:flex; align-items:center; gap:4px; background:var(--vidro); backdrop-filter:blur(10px);
    -webkit-backdrop-filter:blur(10px); border-radius:999px; padding:6px 6px 6px 18px; box-shadow:0 8px 24px rgba(59,31,122,.18); }
  .busca input[type="text"] { flex:1; min-width:0; border:0; outline:0; background:transparent; font-size:1rem; color:var(--escuro); padding:10px 0; }
  .busca input::placeholder { color:rgba(59,31,122,.55); }
  .icone { width:42px; height:42px; border:0; border-radius:50%; background:transparent; color:var(--roxo); display:grid; place-items:center; cursor:pointer; flex-shrink:0; }
  .icone svg { width:22px; height:22px; }
  .icone:focus-visible, .pilula:focus-visible, select:focus-visible { outline:3px solid var(--roxo); outline-offset:2px; }
  .icone.gravando { background:#e5484d; color:var(--branco); }
  .enviar { background:var(--roxo); color:var(--branco); }
  nav { margin-top:14px; display:flex; gap:8px; }
  .pilula { border:0; cursor:pointer; font-size:.9rem; font-weight:600; padding:10px 18px; border-radius:999px; background:rgba(255,255,255,.5); color:var(--escuro); }
  .pilula.ativa { background:var(--roxo); color:var(--branco); }
</style>
</head>
<body>
  <div class="logo">HOPE-IA</div>

  <main>
    <h1>HOPE-IA</h1>
    <p class="sub">Tecnologia Brasil</p>
    <svg class="cerebro" viewBox="0 0 240 180" role="img" aria-label="Nuvem com cérebro">
      <defs>
        <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e3d6fb"/></linearGradient>
        <linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8d63e6"/><stop offset="1" stop-color="#5b2fb8"/></linearGradient>
      </defs>
      <path d="M62 150c-26 0-46-17-46-40 0-20 15-36 35-39 3-27 27-47 55-47 22 0 41 12 50 30 4-2 9-3 14-3 25 0 45 18 45 42 0 31-26 57-60 57z" fill="url(#g1)"/>
      <g fill="url(#g2)" opacity="0.95">
        <path d="M120 62c-9-9-26-5-29 8-9 1-15 9-13 18-6 5-6 14 0 19-1 9 6 17 15 17 6 6 17 5 22-2z"/>
        <path d="M120 62c9-9 26-5 29 8 9 1 15 9 13 18 6 5 6 14 0 19 1 9-6 17-15 17-6 6-17 5-22-2z"/>
      </g>
      <g fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round">
        <path d="M120 64v58"/>
        <path d="M101 84c6 0 10 4 10 10M139 84c-6 0-10 4-10 10M104 108c5-1 9 2 10 6M136 108c-5-1-9 2-10 6"/>
      </g>
    </svg>
  </main>

  <div id="conversa" aria-live="polite"></div>

  <div class="seletor">
    <select id="modelo" aria-label="Escolher IA">
      <option value="openrouter/auto">Automático (escolhe a melhor IA)</option>
    </select>
  </div>

  <form class="busca" id="formulario" autocomplete="off">
    <input type="text" id="texto" placeholder="Pergunte qualquer coisa à Hope-IA" aria-label="Mensagem">
    <button type="button" class="icone" id="botaoMic" aria-label="Falar com a Hope-IA">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
    </button>
    <button type="button" class="icone" id="botaoCamera" aria-label="Enviar foto">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>
    </button>
    <button type="submit" class="icone enviar" aria-label="Enviar mensagem">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </button>
    <input type="file" id="arquivo" accept="image/*" capture="environment" hidden>
  </form>

  <nav aria-label="Menu">
    <button class="pilula ativa" type="button">Conversar</button>
    <button class="pilula" type="button">Criar</button>
    <button class="pilula" type="button">Histórico</button>
  </nav>

<script>
  const formulario = document.getElementById("formulario");
  const campo = document.getElementById("texto");
  const conversa = document.getElementById("conversa");
  const botaoMic = document.getElementById("botaoMic");
  const botaoCamera = document.getElementById("botaoCamera");
  const arquivo = document.getElementById("arquivo");
  const seletor = document.getElementById("modelo");
  let historico = [];

  function adicionar(tipo, texto) {
    document.body.classList.add("conversando");
    const el = document.createElement("div");
    el.className = "msg " + tipo;
    el.textContent = texto;
    conversa.appendChild(el);
    conversa.scrollTop = conversa.scrollHeight;
    return el;
  }

  async function carregarModelos() {
    try {
      const r = await fetch("/api/modelos");
      const dados = await r.json();
      const grupos = {};
      (dados.modelos || []).forEach((m) => {
        (grupos[m.grupo] = grupos[m.grupo] || []).push(m);
      });
      Object.keys(grupos).forEach((nome) => {
        const og = document.createElement("optgroup");
        og.label = nome;
        grupos[nome].forEach((m) => {
          const op = document.createElement("option");
          op.value = m.id;
          op.textContent = m.nome;
          og.appendChild(op);
        });
        seletor.appendChild(og);
      });
    } catch (e) {
      /* mantém só a opção Automático */
    }
  }
  carregarModelos();

  formulario.addEventListener("submit", async (e) => {
    e.preventDefault();
    const mensagem = campo.value.trim();
    if (!mensagem) return;
    adicionar("eu", mensagem);
    campo.value = "";
    historico.push({ role: "user", content: mensagem });
    const espera = adicionar("ia", "Pensando...");
    try {
      const r = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ modelo: seletor.value, mensagens: historico.slice(-12) })
      });
      const dados = await r.json();
      const texto = dados.resposta || dados.erro || "Sem resposta.";
      espera.textContent = texto;
      if (dados.resposta) historico.push({ role: "assistant", content: dados.resposta });
    } catch (erro) {
      espera.textContent = "Não consegui falar com o servidor. Tente de novo.";
    }
  });

  botaoCamera.addEventListener("click", () => arquivo.click());
  arquivo.addEventListener("change", () => {
    if (arquivo.files.length) adicionar("eu", "Foto anexada: " + arquivo.files[0].name + " (envio de imagens ainda não está ligado)");
  });

  const Reconhecimento = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (Reconhecimento) {
    const voz = new Reconhecimento();
    voz.lang = "pt-BR";
    voz.interimResults = false;
    voz.onresult = (ev) => { campo.value = ev.results[0][0].transcript; };
    voz.onend = () => botaoMic.classList.remove("gravando");
    botaoMic.addEventListener("click", () => { botaoMic.classList.add("gravando"); voz.start(); });
  } else {
    botaoMic.addEventListener("click", () => adicionar("ia", "Este navegador não tem reconhecimento de voz. Use o Chrome."));
  }
</script>
</body>
</html>
"""


@app.route("/")
def inicio():
    return Response(INTERFACE_HTML, mimetype="text/html")


@app.route("/api/modelos")
def modelos():
    agora = time.time()
    if _cache["lista"] and agora - _cache["hora"] < 3600:
        return jsonify({"modelos": _cache["lista"]})
    try:
        dados = pedir(OPENROUTER + "/models", tempo=20)
        lista = []
        for m in dados.get("data", []):
            id_modelo = m.get("id", "")
            dono = id_modelo.split("/")[0]
            if dono in FORNECEDORES and not id_modelo.endswith(":free"):
                lista.append({
                    "id": id_modelo,
                    "nome": m.get("name") or id_modelo,
                    "grupo": FORNECEDORES[dono],
                })
        lista.sort(key=lambda x: (x["grupo"], x["nome"]))
        _cache["hora"] = agora
        _cache["lista"] = lista
        return jsonify({"modelos": lista})
    except Exception:
        return jsonify({"modelos": []})


@app.route("/api/chat", methods=["POST"])
def chat():
    corpo = request.get_json(silent=True) or {}
    modelo = corpo.get("modelo") or "openrouter/auto"
    mensagens = [
        {"role": m.get("role"), "content": str(m.get("content", ""))[:8000]}
        for m in (corpo.get("mensagens") or [])[-12:]
        if m.get("role") in ("user", "assistant")
    ]
    if not mensagens:
        return jsonify({"erro": "Escreva uma mensagem."}), 400

    chave = os.environ.get("OPENROUTER_API_KEY")
    if not chave:
        return jsonify({"erro": "Falta a chave OPENROUTER_API_KEY na Vercel (Settings > Environment Variables)."}), 500

    try:
        dados = pedir(
            OPENROUTER + "/chat/completions",
            {"model": modelo, "messages": [{"role": "system", "content": SISTEMA}] + mensagens},
            chave=chave,
        )
        texto = dados["choices"][0]["message"]["content"]
        return jsonify({"resposta": texto})
    except urllib.error.HTTPError as e:
        try:
            detalhe = json.loads(e.read().decode()).get("error", {}).get("message", "")
        except Exception:
            detalhe = ""
        return jsonify({"erro": "Erro " + str(e.code) + " do OpenRouter. " + detalhe}), 502
    except Exception:
        return jsonify({"erro": "Não consegui falar com a IA agora. Tente outro modelo."}), 502


@app.route("/saude")
def saude():
    return jsonify({"status": "ok", "chave": bool(os.environ.get("OPENROUTER_API_KEY"))})
