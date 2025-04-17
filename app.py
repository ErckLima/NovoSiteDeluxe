from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def load_iphones():
    try:
        caminho = os.path.join('static', 'iphones.json')
        with open(caminho, 'r', encoding='utf-8') as file:
            iphones = json.load(file)
        return iphones if isinstance(iphones, list) else []
    except Exception as e:
        print(f"Erro ao carregar dados do arquivo: {e}")
        return []

@app.route('/')
def home():
    iphones = load_iphones()
    return render_template('index.html', iphones=iphones)


if __name__ == '__main__':
    app.run(debug=True)
