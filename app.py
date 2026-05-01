from flask import Flask
# 1. Importar o Blueprint que você criou lá no views.py
from routes.views import views_bp 

app = Flask(__name__)

# 2. Registrar o Blueprint (conectar os fios)
app.register_blueprint(views_bp)

if __name__ == "__main__":
    app.run(debug=True)