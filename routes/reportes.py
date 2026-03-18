from flask import Blueprint, render_template
from flask_login import login_required

from extensions import db
from models.client import Cliente
from models.service import Servicio
from models.user import Usuario

reportes_bp = Blueprint('reportes', __name__)


cliente_servicio = db.Table(
    'cliente_servicio',
    db.Column('cliente_id', db.Integer, db.ForeignKey('clientes.id'), primary_key=True),
    db.Column('servicio_id', db.Integer, db.ForeignKey('servicios.id'), primary_key=True),
    db.Column('fecha_asignacion', db.DateTime, default=db.func.current_timestamp())
)


@reportes_bp.route('/reportes')
@login_required
def reportes():
    servicios_populares = db.session.query(
        Servicio.nombre,
        db.func.count(cliente_servicio.c.servicio_id).label('total')
    ).join(cliente_servicio).group_by(Servicio.id).order_by(db.desc('total')).limit(5).all()

    clientes_top = db.session.query(
        Cliente.nombre,
        Cliente.email,
        db.func.count(cliente_servicio.c.cliente_id).label('total_servicios')
    ).join(cliente_servicio).group_by(Cliente.id).order_by(db.desc('total_servicios')).limit(5).all()

    ingresos_totales = db.session.query(
        db.func.sum(Servicio.precio)
    ).join(cliente_servicio).scalar() or 0

    total_asignaciones = db.session.query(cliente_servicio).count()

    return render_template(
        'reportes.html',
        servicios_populares=servicios_populares,
        clientes_top=clientes_top,
        ingresos_totales=ingresos_totales,
        total_asignaciones=total_asignaciones
    )