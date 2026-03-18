from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from extensions import db
from models.user import Usuario

usuarios_bp = Blueprint('usuarios', __name__)


def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.rol != 'admin':
            flash('Acceso denegado. Se requieren permisos de administrador.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@usuarios_bp.route('/usuarios')
@login_required
@admin_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios_lista.html', usuarios=usuarios)


@usuarios_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    
    if request.method == 'POST':
        usuario.username = request.form.get('username')
        usuario.email = request.form.get('email')
        usuario.nombre_completo = request.form.get('nombre_completo')
        usuario.rol = request.form.get('rol')
        
        nueva_password = request.form.get('password')
        if nueva_password:
            usuario.set_password(nueva_password)
        
        db.session.commit()
        flash(f'Usuario {usuario.username} actualizado correctamente', 'success')
        return redirect(url_for('usuarios.listar_usuarios'))
    
    return render_template('usuario_form.html', usuario=usuario, editar=True)


@usuarios_bp.route('/usuarios/eliminar/<int:id>')
@login_required
@admin_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    
    if usuario.id == current_user.id:
        flash('No puedes eliminar tu propio usuario', 'danger')
        return redirect(url_for('usuarios.listar_usuarios'))
    
    db.session.delete(usuario)
    db.session.commit()
    flash(f'Usuario {usuario.username} eliminado', 'success')
    return redirect(url_for('usuarios.listar_usuarios'))