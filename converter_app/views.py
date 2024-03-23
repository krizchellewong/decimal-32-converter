from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired 
from . import app   
from .converter import decimal_32_floating_ponint_converter as Converter


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
        return render_template("index.html", number = converted, form=form)
        
    return render_template("index.html", form = form)


# Class for the form submission
class ConvertForm(FlaskForm):
    choices = [('roundup', 'Round up'),
               ('rounddown', 'Round down'),
               ('tiestoeven', 'Ties to even')]

    decimal_field = FloatField('Number', validators=[DataRequired()])
    exponent = IntegerField('10^', validators=[DataRequired()])
    rounding = SelectField('Rounding Option:', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Submit')