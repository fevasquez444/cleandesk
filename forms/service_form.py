from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ServicioForm(FlaskForm):
    nombre = StringField('Nombre del Servicio', validators=[DataRequired()])
    descripcion = StringField('Descripción')
    precio = FloatField('Precio', validators=[DataRequired()])
    duracion = StringField('Duración')
    submit = SubmitField('Guardar Servicio')
