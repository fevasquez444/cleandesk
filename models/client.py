from extensions import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    servicios = db.relationship(
        'Servicio',
        secondary='cliente_servicio',
        backref=db.backref('clientes', lazy='dynamic'),
        lazy='dynamic'
    )
    
    def __repr__(self):
        return f'<Cliente {self.nombre}>'