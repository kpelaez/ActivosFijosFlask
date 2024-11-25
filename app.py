from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
# # Importacion para los tableros de dash
# import dash
# from dash import dcc, html
# import plotly.express as px
# import pandas as pd
from dash_app import create_dash_app

# Instanciamos los objetos para crear la base de datos y las migraciones 
db  = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app, resources={r"/*":{"origins": "http://localhost:3000"}})
    # db.init_app(app)
    # migrate.init_app(app, db)

    #Integrar Dash
    create_dash_app(app)

    from activos_fijos.routes import activos_fijos_bp
    app.register_blueprint(activos_fijos_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)