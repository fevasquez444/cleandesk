from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # ¡CORREGIDO!
from flask_migrate import Migrate
from forms import ClientForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-cambia-me-en-produccion'

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleandesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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


if __name__ == '__main__':
    app.run(debug=True)