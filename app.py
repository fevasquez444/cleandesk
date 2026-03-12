from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import ClientForm
from services_forms import ServicioForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-cambia-me-en-produccion'


# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleandesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializar extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # La vista a la que redirige si no está autenticado
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'
login_manager.login_message_category = 'info'


# MODELO DE DATOS (esto estaba faltando)
class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return f'<Cliente {self.nombre}>'


# RUTA PRINCIPAL (esto estaba faltando)
@app.route('/')
def index():
    return render_template('index.html')


# RUTA PARA NUEVO CLIENTE
@app.route('/clientes/nuevo', methods=['GET', 'POST'])
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
        return redirect(url_for('index'))
    return render_template('cliente_form.html', form=form)


# MODELO DE SERVICIOS (nuevo)
class Servicio(db.Model):
    __tablename__ = 'servicios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float, nullable=False)
    duracion = db.Column(db.String(50))  # ej: "2 horas", "1 día"
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return f'<Servicio {self.nombre}>'
    
# MODELO DE DATOS PARA USUARIO (NUEVO)
class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nombre_completo = db.Column(db.String(100))
    rol = db.Column(db.String(20), default='empleado')  # 'admin' o 'empleado'
    activo = db.Column(db.Boolean, default=True)
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return f'<Usuario {self.username}>'

# RUTA PARA LOGIN DE USUARIO
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))


# RUTA PARA EDITAR CLIENTE (NUEVA)
@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    # Buscar el cliente por ID o mostrar 404 si no existe
    cliente = Cliente.query.get_or_404(id)
    
    # Crear el formulario y cargar los datos del cliente
    form = ClientForm(obj=cliente)
    
    if form.validate_on_submit():
        # Actualizar los campos del cliente con los datos del formulario
        form.populate_obj(cliente)
        db.session.commit()
        return redirect(url_for('listar_clientes'))
    
    return render_template('cliente_form.html', form=form, editar=True, cliente=cliente)


# RUTA PARA ELIMINAR CLIENTE (NUEVA)
@app.route('/clientes/eliminar/<int:id>')
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('listar_clientes'))


# RUTA PARA LISTAR CLIENTES (NUEVA)
@app.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes_lista.html', clientes=clientes)

from services_forms import ServicioForm  # <-- Agrega esto al principio con las otras importaciones

# ===== RUTAS PARA SERVICIOS =====

# LISTA TODOS LOS SERVICIOS
@app.route('/servicios')
def listar_servicios():
    servicios = Servicio.query.all()
    return render_template('servicios_lista.html', servicios=servicios)

# CREAR UN NUEVO SERVICIO
@app.route('/servicios/nuevo', methods=['GET', 'POST'])
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
        return redirect(url_for('listar_servicios'))
    return render_template('servicio_form.html', form=form, editar=False)

# EDITAR UN SERVICIO
@app.route('/servicios/editar/<int:id>', methods=['GET', 'POST'])
def editar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    form = ServicioForm(obj=servicio)
    
    if form.validate_on_submit():
        form.populate_obj(servicio)
        db.session.commit()
        return redirect(url_for('listar_servicios'))
    
    return render_template('servicio_form.html', form=form, editar=True, servicio=servicio)

# ELIMINAR UN SERVICIO
@app.route('/servicios/eliminar/<int:id>')
def eliminar_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    db.session.delete(servicio)
    db.session.commit()
    return redirect(url_for('listar_servicios'))


# ===== RUTAS DE AUTENTICACIÓN =====

# REGISTRO DE USUARIOS
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        nombre_completo = request.form.get('nombre_completo')
        
        # Verificar si el usuario ya existe
        usuario_existe = Usuario.query.filter_by(username=username).first()
        email_existe = Usuario.query.filter_by(email=email).first()
        
        if usuario_existe:
            flash('El nombre de usuario ya existe', 'danger')
        elif email_existe:
            flash('El email ya está registrado', 'danger')
        else:
            # Crear nuevo usuario (sin hash aún, después implementaremos)
            nuevo_usuario = Usuario(
                username=username,
                email=email,
                password=password,  # TEMPORAL: después agregaremos hash
                nombre_completo=nombre_completo,
                rol='empleado'
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario registrado correctamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
    
    return render_template('registro.html')


# LOGIN DE USUARIOS
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(username=username).first()
        
        if usuario and usuario.password == password:  # TEMPORAL: después mejoraremos
            login_user(usuario)
            flash(f'Bienvenido, {usuario.nombre_completo or usuario.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html')


# LOGOUT
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('index'))


# PERFIL DE USUARIO
@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', usuario=current_user)


if __name__ == '__main__':
    app.run(debug=True)