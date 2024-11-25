from app import db

class ActivoFijo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    descripcion = db.Column(db.Text, nullable = True)
    fecha_compra = db.Column(db.Date, nullable = False)
    valor = db.Column(db.Float, nullable = False)

