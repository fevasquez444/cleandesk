from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from extensions import db
from forms.client_form import ClientForm
from models.client import Cliente

clientes_bp = Blueprint('clientes', __name__)


@clientes_bp.route('/clientes')
@login_required
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes_lista.html', clientes=clientes)


@clientes_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_cliente():
    form = ClientForm()
    if form.validate_on_submit():
        cliente = Cliente(
            nombre=form.nombre.data,
            email=form.email.data,
            telefono=form.telefono.data,
            direccion=form.direccion.data
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('cliente_form.html', form=form)


@clientes_bp.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    form = ClientForm(obj=cliente)

    if form.validate_on_submit():
        form.populate_obj(cliente)
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('cliente_form.html', form=form, editar=True, cliente=cliente)


@clientes_bp.route('/clientes/eliminar/<int:id>')
@login_required
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.listar_clientes'))