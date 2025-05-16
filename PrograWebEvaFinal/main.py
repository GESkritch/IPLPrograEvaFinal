from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total = cantidad * precio_unitario

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        total_descuento = total * (1 - descuento)

        descuento_aplicado = total - total_descuento

        return render_template('resultado.html',
                               tipo='compra',
                               nombre=nombre,
                               total=total,
                               descuento_aplicado=descuento_aplicado,
                               total_descuento=total_descuento)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        credenciales = {
            'juan': 'admin',
            'pepe': 'user'
        }

        if usuario in credenciales and credenciales[usuario] == clave:
            rol = 'administrador' if usuario == 'juan' else 'usuario'
            mensaje = f'Bienvenido {rol} {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('resultado.html', tipo='login', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
