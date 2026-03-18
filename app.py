import os
from functools import wraps

from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_login import login_required, current_user

from extensions import db, bcrypt, login_manager
from routes.clientes import clientes_bp
from routes.servicios import servicios_bp
from routes.auth import auth_bp
from forms.asignar_form import AsignarServicioForm

from models.client import Cliente
from models.service import Servicio
from models.user import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-secreta-por-defecto')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleandesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'
login_manager.login_message_category = 'info'

bcrypt.init_app(app)

app.register_blueprint(clientes_bp)
app.register_blueprint(servicios_bp)
app.register_blueprint(auth_bp)

# ===== DECORADOR PARA VERIFICAR SI EL USUARIO ES ADMIN =====

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.rol != 'admin':
            flash('Acceso denegado. Se requieren permisos de administrador.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
# ===== FIN DEL DECORADOR =====


# RUTA PRINCIPAL (esto estaba faltando)
@app.route('/')
def index():
    # Obtener estadísticas para el dashboard
    total_clientes = Cliente.query.count()
    total_servicios = Servicio.query.count()
    total_usuarios = Usuario.query.count()
    
    # Contar admins y empleados
    admins = Usuario.query.filter_by(rol='admin').count()
    empleados = Usuario.query.filter_by(rol='empleado').count()
    
    # Últimos 5 clientes registrados
    ultimos_clientes = Cliente.query.order_by(Cliente.fecha_registro.desc()).limit(5).all()
    
    return render_template('index.html', 
                          total_clientes=total_clientes,
                          total_servicios=total_servicios,
                          total_usuarios=total_usuarios,
                          admins=admins,
                          empleados=empleados,
                          ultimos_clientes=ultimos_clientes)
    
    
# ===== TABLA INTERMEDIA (NUEVA) =====
cliente_servicio = db.Table('cliente_servicio',
    db.Column('cliente_id', db.Integer, db.ForeignKey('clientes.id'), primary_key=True),
    db.Column('servicio_id', db.Integer, db.ForeignKey('servicios.id'), primary_key=True),
    db.Column('fecha_asignacion', db.DateTime, default=db.func.current_timestamp())
)


# RUTA PARA LOGIN DE USUARIO
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))


# ===== ADMINISTRACIÓN DE USUARIOS =====

@app.route('/usuarios')
@login_required
@admin_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios_lista.html', usuarios=usuarios)

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
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
        return redirect(url_for('listar_usuarios'))
    
    return render_template('usuario_form.html', usuario=usuario, editar=True)

@app.route('/usuarios/eliminar/<int:id>')
@login_required
@admin_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    
    if usuario.id == current_user.id:
        flash('No puedes eliminar tu propio usuario', 'danger')
        return redirect(url_for('listar_usuarios'))
    
    db.session.delete(usuario)
    db.session.commit()
    flash(f'Usuario {usuario.username} eliminado', 'success')
    return redirect(url_for('listar_usuarios'))


# ===== RUTAS PARA REPORTES Y ESTADÍSTICAS =====

@app.route('/reportes')
@login_required
def reportes():
    # 1. Servicios más contratados (top 5)
    servicios_populares = db.session.query(
        Servicio.nombre,
        db.func.count(cliente_servicio.c.servicio_id).label('total')
    ).join(cliente_servicio).group_by(Servicio.id).order_by(db.desc('total')).limit(5).all()
    
    # 2. Clientes con más servicios (top 5)
    clientes_top = db.session.query(
        Cliente.nombre,
        Cliente.email,
        db.func.count(cliente_servicio.c.cliente_id).label('total_servicios')
    ).join(cliente_servicio).group_by(Cliente.id).order_by(db.desc('total_servicios')).limit(5).all()
    
    # 3. Ingresos totales (suma de precios de todos los servicios asignados)
    ingresos_totales = db.session.query(
        db.func.sum(Servicio.precio)
    ).join(cliente_servicio).scalar() or 0
    
    # 4. Total de asignaciones
    total_asignaciones = db.session.query(cliente_servicio).count()
    
    return render_template('reportes.html',
                          servicios_populares=servicios_populares,
                          clientes_top=clientes_top,
                          ingresos_totales=ingresos_totales,
                          total_asignaciones=total_asignaciones)
    
    
if __name__ == '__main__':
    app.run(debug=True)