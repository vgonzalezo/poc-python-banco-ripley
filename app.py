from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():  
    return render_template("index.html")

@app.route("/SimuladorCampanas/combos/productos", methods=['GET', 'POST'])
@app.route("/SimuladorCampanas/combos/sucursales", methods=['GET', 'POST'])
@app.route("/SimuladorCampanas/combos/canales", methods=['GET', 'POST'])
def productos():
    return ""

@app.route("/SimuladorCampanas/CaptacionOnline/captarCliente", methods=['GET', 'POST'])
def captarCliente():
    response = '{"codigoError":0,"respuesta":{"codTexto":[{"codigo":4,"texto":"01"},{"codigo":2,"texto":" #1C**********************************************#1B#1IFELICITACIONES!#1ITienes preaprobada una #1ITarjeta Ripley MasterCard#1I\n#1B#1I(*) Sujeto a Evaluacion.#1B#1C**********************************************"},{"codigo":1,"texto":"#CLIENTE CAMBIO A TARJETA MASTERCARD#  # #Ofrece al cliente#\n#cambiar su actualTarjeta RIPLEY#\n#a Tarjeta RIPLEY MASTERCARD#\n#Emitir Tarjeta?"},{"codigo":3,"texto":"X"}]},"textoError":"Exito"}'
    return json.loads(response, strict=False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)