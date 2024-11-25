from flask import Blueprint, request, jsonify
from app import db
from activos_fijos.models import ActivoFijo

activos_fijos_bp = Blueprint('activos_fijos',__name__)

@activos_fijos_bp.route('/api/ping', methods = ['GET'])
def ping():
    return jsonify({'message': 'Pong! El backend esta funcionando correctamente'}), 200

@activos_fijos_bp.route('/activos',  methods = ['GET'])
def obtener_activos():
    activos = ActivoFijo.query.all()
    return jsonify([activo for activo in activos])

@activos_fijos_bp.route('/activos', methods=['POST'])
def crear_activo():
    data = request.get_json()
    nuevo_activo = ActivoFijo(**data)
    db.session.add(nuevo_activo)
    db.session.commit()
    return jsonify({'message': 'Activo creado exitosamente'}), 201