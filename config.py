import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://administrador:Harumi2023@localhost/gestion_activos_fijos')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

