from flask import Flask, render_template_string

 app = Flask(__name__)

# Interface web da HOPE-IA Tecnologia do Brasil
interface_html = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HOPE-IA - Tecnologia do Brasil</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: #1e293b;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            max-width: 600px;
            width: 90%;
        }
        h1 {
            color: #38bdf8;
            margin-bottom: 10px;
        }
        p {
            color: #94a3b8;
            font-size: 1.1rem;
        }
        .status {
            margin-top: 20px;
            display: inline-block;
            background: #22c55e;
            color: #fff;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>HOPE-IA</h1>
        <p>Tecnologia do Brasil na Nuvem</p>
        <div class="status">● Sistema Online e Operacional</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(interface_html)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
