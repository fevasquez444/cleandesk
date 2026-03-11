from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Optional

class ServicioForm(FlaskForm):
    nombre = StringField('Nombre del Servicio', validators=[DataRequired()])
    descripcion = StringField('Descripción', validators=[Optional()])
    precio = FloatField('Precio ($)', validators=[DataRequired()])
    duracion = StringField('Duración (ej: 2 horas)', validators=[Optional()])
    submit = SubmitField('Guardar Servicio')