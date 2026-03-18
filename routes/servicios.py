from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from extensions import db
from forms.service_form import ServicioForm
from models.service import Servicio

servicios_bp = Blueprint('servicios', __name__)

@servicios_bp.route('/servicios')
@login_required
def listar_servicios():
    servicios = Servicio.query.all()
    return render_template('servicios_lista.html', servicios=servicios)

@servicios_bp.route('/servicios/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_servicio():
    form = ServicioForm()
    if form.validate_on_submit():
        servicio = Servicio(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            precio=form.precio.data,
            duracion=form.duracion.data
        )
        db.session.add(servicio)
        db.session.commit()
        return redirect(url_for('servicios.listar_servicios'))
    return render_template('servicio_form.html', form=form, editar=False)

@servicios_bp.route('/servicios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    form = ServicioForm(obj=servicio)

    if form.validate_on_submit():
        form.populate_obj(servicio)
        db.session.commit()
        return redirect(url_for('servicios.listar_servicios'))

    return render_template('servicio_form.html', form=form, editar=True, servicio=servicio)

@servicios_bp.route('/servicios/eliminar/<int:id>')
@login_required
def eliminar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    db.session.delete(servicio)
    db.session.commit()
    return redirect(url_for('servicios.listar_servicios'))