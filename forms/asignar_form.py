from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class AsignarServicioForm(FlaskForm):
    servicio = SelectField('Seleccionar Servicio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Asignar Servicio')
