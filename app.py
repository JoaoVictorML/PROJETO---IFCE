from flask import Flask, render_template

app = Flask(__name__)

# 1. Rota para a Página Inicial (index.html)
@app.route('/')
def index():
    # O Flask vai procurar o arquivo index.html automaticamente dentro da pasta 'templates'
    return render_template('index.html')

# 2. Rota para a Página de Dashboard (dashboard.html)
@app.route('/dashboard')
def dashboard():
    # Se o arquivo estiver dentro de uma subpasta, basta passar o caminho relativo
    return render_template('dashboard.html')

# Passo fundamental para rodar o servidor local
if __name__ == '__main__':
    app.run(debug=True)