from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired 
from . import app   

# Index route
@app.route("/", methods = ['GET', 'POST'])
def home():
    form = ConvertForm() # Initialize form

    if request.method == 'POST' and form.validate():
        # TODO: the request should display the output of the decimal-32 conversion
        return render_template("index.html", number = form.decimal_field.data, form=form)
    return render_template("index.html", form = form)


# Class for the form submission
class ConvertForm(FlaskForm):
    decimal_field = FloatField('Number', validators=[DataRequired()])
    exponent = IntegerField('10^', validators=[DataRequired()])
    submit = SubmitField('Submit')