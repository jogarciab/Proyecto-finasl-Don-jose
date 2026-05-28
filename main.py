from flask import Flask, render_template

app = Flask(__name__)

# PAGINA PRINCIPAL APP
@app.route("/")
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