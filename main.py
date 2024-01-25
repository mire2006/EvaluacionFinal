from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    total_sin_descuento = 0
    descuento = 0
    total_con_descuento = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15 * total_sin_descuento
        elif edad > 30:
            descuento = 0.25 * total_sin_descuento

        total_con_descuento = total_sin_descuento - descuento

    return render_template('ejercicio1.html', nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           descuento=descuento,
                           total_con_descuento=total_con_descuento)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = ""
    category = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "juan" and password == "admin":
            message = f"Bienvenido administrador {username}"
            category = "admin"
        elif username == "pepe" and password == "user":
            message = f"Bienvenido usuario {username}"
            category = "user"
        else:
            message = "Usuario o contraseña incorrectos"
            category = "error"

    return render_template('ejercicio2.html', message=message, category=category)

if __name__ == '__main__':
    app.run(debug=True)
