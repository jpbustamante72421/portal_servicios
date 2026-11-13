from flask import Flask, render_template, request

app = Flask(__name__)

# PAGINA DE INICIO
@app.route('/')
def inicio():
    return render_template('index.html')


# CALCULADORA DE COMPRA
@app.route('/compra', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST':
        cantidad = float(request.form['cantidad'])
        precio = float(request.form['precio'])

        subtotal = cantidad * precio

        if subtotal > 1000:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        total = subtotal - descuento

        return render_template(
            'compra.html',
            cantidad=cantidad,
            precio=precio,
            subtotal=subtotal,
            descuento=descuento,
            total=total
        )

    return render_template('compra.html')


# CALCULADORA DE SALARIO
@app.route('/salario', methods=['GET', 'POST'])
def salario():
    if request.method == 'POST':
        horas = float(request.form['horas'])
        pago = float(request.form['pago'])

        if horas <= 40:
            salario_total = horas * pago
        else:
            horas_extra = horas - 40
            salario_total = (40 * pago) + (horas_extra * pago * 2)

        return render_template(
            'salario.html',
            horas=horas,
            pago=pago,
            salario_total=salario_total
        )

    return render_template('salario.html')


# CONVERSOR DE TEMPERATURA
@app.route('/temperatura', methods=['GET', 'POST'])
def temperatura():
    if request.method == 'POST':
        celsius = float(request.form['celsius'])

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        return render_template(
            'temperatura.html',
            celsius=celsius,
            fahrenheit=fahrenheit,
            kelvin=kelvin
        )

    return render_template('temperatura.html')


# INFORMACION DE LA EMPRESA
@app.route('/empresa')
def empresa():
    return render_template('empresa.html')


# SERVICIOS
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


# CONTACTO
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)