from flask import Flask, render_template, request, make_response
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, IntegerField, RadioField, HiddenField
from wtforms.validators import DataRequired 
from . import app   
from .converter import decimal_32_floating_point_converter as Converter
from .converter import hex_converter as HexConverter

# Index route
@app.route("/", methods = ['GET', 'POST'])
def home():
    form = ConvertForm() # Initialize form

    if request.method == 'POST' and form.validate():
        decimal = form.decimal_field.data
        exponent = form.exponent.data
        rounding = form.rounding.data
        converted = Converter(decimal, exponent, rounding)
        hex_converted = HexConverter(converted[0])
        print(f"HEX CONVERTED VALUE !!!!!!: {hex_converted}")
        return render_template("index.html", decimal_number=decimal, exponent=exponent, binary_conversion = converted[0], hex = f"0x{hex_converted}", form=form)
        
    return render_template("index.html", form = form)

# Route to handle file download
@app.route("/download", methods=['GET'])
def download_file():
    # Retrieve binary_conversion and hex values from the query parameters
    decimal_number = request.args.get('decimal_number', '')
    exponent = request.args.get('exponent', '')
    binary_conversion = request.args.get('binary_conversion', '')
    hex_value = request.args.get('hex', '')

    # Generate content for the text file
    content = f"Decimal Number: {decimal_number}\nExponent: {exponent}\nBinary Conversion: {binary_conversion}\nHex Value: {hex_value}\n"

    # Create a response object with the file content
    response = make_response(content)
    
    # Set the appropriate headers to trigger file download
    response.headers['Content-Disposition'] = 'attachment; filename=conversion_results.txt'
    response.headers['Content-Type'] = 'text/plain'

    return response

# Class for the form submission
class ConvertForm(FlaskForm):
    choices = [('round-up', 'Round up'),
               ('round-down', 'Round down'),
               ('truncate', 'Truncate'),
               ('ties-to-even', 'Ties to even')]

    decimal_field = FloatField('Decimal Number', validators=[DataRequired()])
    exponent = IntegerField('Exponent', validators=[DataRequired()])
    rounding = RadioField('Rounding Option:', choices=choices)
    submit = SubmitField('Submit')