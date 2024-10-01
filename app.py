from flask import Flask, render_template, request, redirect, session

from models.productos import Productos
from models.carrito import Carrito_Builer

app = Flask(__name__, static_folder='static', template_folder='templates')

app.secret_key = "P4S$W0rd"

@app.route('/', methods=['GET'])
def home():
    return render_template('index1.html')

@app.route('/inicio')
def home1():
    return render_template('inicio.html')

@app.route('/aislante')
def home3():
    return render_template('apartado_cada_tipo/aislante.html')

@app.route('/cemento')
def home4():
    return render_template('apartado_cada_tipo/cemento.html')

@app.route('/general')
def home5():
    return render_template('apartado_cada_tipo/general.html')

@app.route('/manuales')
def home6():
    return render_template('apartado_cada_tipo/manuales.html')

@app.route('/herramientas')
def home7():
    return render_template('apartado_cada_tipo/herramientas.html')

@app.route('/metalcon')
def home8():
    return render_template('apartado_cada_tipo/metalcon.html')

@app.route('/pinturas')
def home9():
    return render_template('apartado_cada_tipo/pinturas.html')

@app.route('/puertas')
def home10():
    return render_template('apartado_cada_tipo/puertas.html')

@app.route('/techumbres')
def home11():
    return render_template('apartado_cada_tipo/techumbres.html')

@app.route('/ventanas')
def home12():
    return render_template('apartado_cada_tipo/ventanas.html')

#logo de la pagina
@app.route('/logo')
def home13():
    return render_template('index1.html')


#carrito
@app.route("/producto/", methods=["GET"])
def proxxo():
    session["id"] = 1
    session["name"] = "jorge"
    productos = Productos.select_all()
    return render_template("productos.html", products=productos)

@app.route("/carrito/", methods=["GET"])
def carrito33():
    usuarios_idusuarios = session["id"]
    elments = Carrito_Builer.select_all(usuarios_idusuarios)
    return render_template("carrito.html", elments=elments)

@app.route("/carrito/add/", methods=["POST"])
def add_product():
    usuarios_idusuarios = session["id"]
    productos_idproductos = request.form.get("productos_idproductos")

    # Revisar si está en el carrito
    print(usuarios_idusuarios, productos_idproductos)
    elmt = Carrito_Builer.get_element(usuarios_idusuarios, productos_idproductos)
    if len(elmt) == 0:
        ## Caso donde hay que insertar
        Carrito_Builer.insert(usuarios_idusuarios, productos_idproductos)
    else:
        elmt = elmt[0]
        ## caso donde hay que actualizar la cantidad
        cant = elmt.cant + 1
        elmt_id = elmt.id
        Carrito_Builer.update_cant(cant, elmt_id)

    print(elmt)
    return redirect("/")

@app.route("/carrito/pay/", methods=["GET"])
def delete_cart():
    usuarios_idusuarios = session["id"]
    Carrito_Builer.delete_cart(usuarios_idusuarios)
    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)
