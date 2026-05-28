from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# PAGINA INICIAL LOGIN
@app.route("/")
def inicio():
    return render_template("login.html")


# VALIDAR LOGIN
@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        if usuario == "admin" and password == "123":
            return redirect("/home")
        else:
            return "Usuario o contraseña incorrectos"
    
    return render_template("login.html")

# PAGINA PRINCIPAL APP
@app.route("/home")
def home():
    return render_template("index.html")
# HISTORIAL DE VENTAS
@app.route("/venta")
def venta():
    return render_template("ventas.html")
# REPORTES
@app.route("/reportes")
def reportes():
    return render_template("reportes.html")
# FACTURACION
@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")
# BUSCAR
@app.route("/buscar")
def buscar():
    return render_template("buscar.html")
# COMPRAS REALIZADAS
@app.route("/compras")
def compras():
    return render_template("compras.html")

if __name__ == "__main__":
    app.run(debug=True)