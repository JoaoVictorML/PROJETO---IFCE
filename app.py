from flask import Flask
from extensions import db  # Importa o db neutro
from routes.views import views_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco com o app
db.init_app(app)

app.register_blueprint(views_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)