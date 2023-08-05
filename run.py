#Importar componentes
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import miformulario
import requests, json
from flask_recaptcha import ReCaptcha # Importar ReCaptcha

#Crear app medante instancia
app = Flask(__name__)
#Configuraciones
app.secret_key = "fabricio"
Bootstrap(app) #Decoramos nuestra app con bootstrap
#Recaptcha
app.config['RECAPTCHA_SITE_KEY'] = '6LfGsIAnAAAAAOaUHzFxYOKqD8u3dklrdj0UtOA5' 
app.config['RECAPTCHA_SECRET_KEY'] = '6LfGsIAnAAAAAAjqsSQ7omjilMsDHwetI9C665XD' 
recaptcha = ReCaptcha(app)

#Rutas de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        return render_template('/index.html', nombre = nombre)
    else:
        return render_template('/index.html')
    
@app.route('/proyectos', methods=['GET'])
def proyectos():
    return render_template('/proyectos.html')

@app.route('/blog', methods=['GET'])
def blog():
    return render_template('/blog.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    
    sitekey = "6LfGsIAnAAAAAOaUHzFxYOKqD8u3dklrdj0UtOA5"

    if request.method == 'POST':
        nombre = request.form['Nombre']
        email = request.form['Email']
        mensaje = request.form['Mensaje']
        respuesta_del_captcha = request.form['g-recaptcha-response']

        if comprobar_humano(respuesta_del_captcha):
           #Si devuelve True
            status = "Exito."
            print (status)
        else:
           #Si devuelve False
            status = "Error, vuelve a comprobar que no eres un robot."
            print (status)
        
    return render_template("contacto.html", sitekey=sitekey)

@app.route('/contacto2', methods=['GET', 'POST'])
def contacto2():
    miform = miformulario()

    if miform.validate_on_submit() and recaptcha.verify():
        print(f"Name:{miform.name.data},Email:{miform.email.data},message:{miform.message.data}")
    else:
        print("Algún dato es invalido")
    return render_template("contacto2.html", form=miform)
        
    return render_template("/contacto2.html", form=miform)


def comprobar_humano(respuesta_del_captcha):
    secret = "6LfGsIAnAAAAAAjqsSQ7omjilMsDHwetI9C665XD"
    payload = {'response':respuesta_del_captcha, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']    

#Ejecucion de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)