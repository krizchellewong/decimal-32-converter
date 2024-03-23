from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired 
from . import app   
from .converter import decimal_32_floating_point_converter as Converter
from .converter import hex_converter as HexConverter

# Index route
@app.route("/", methods = ['GET', 'POST'])
def home():
    form = ConvertForm() # Initialize form

    if request.method == 'POST' and form.validate():
        # TODO: the request should display the output of the decimal-32 conversion
        decimal = form.decimal_field.data
        exponent = form.exponent.data
        rounding = form.rounding.data
        converted = Converter(decimal, exponent, rounding)
        hex_converted = HexConverter(converted[0])
        print(f"HEX CONVERTED VALUE !!!!!!: {hex_converted}")
        return render_template("index.html", binary_conversion = converted[0], hex = f"0x{hex_converted}", form=form)
        
    return render_template("index.html", form = form)


# Class for the form submission
class ConvertForm(FlaskForm):
    choices = [('round-up', 'Round up'),
               ('round-down', 'Round down'),
               ('truncate', 'Truncate'),
               ('ties-to-even', 'Ties to even')]

    decimal_field = FloatField('Number', validators=[DataRequired()])
    exponent = IntegerField('10^', validators=[DataRequired()])
    rounding = RadioField('Rounding Option:', choices=choices)
    submit = SubmitField('Submit')