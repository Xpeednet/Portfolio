#Importar componentes
from flask import Flask, render_template

#Crear app medante instancia de clase Flask
app=Flask(__name__)

#Rutas de la aplicación
@app.route('/', methods=['GET'])
def holamundo():
    return render_template('index.html')

@app.route('/proyectos', methods=['GET'])
def misproyectos():
    return render_template('proyectos.html')

@app.route('/blog', methods=['GET'])
def miblog():
    return render_template('blog.html')

@app.route('/contacto', methods=['GET'])
def misproyectos():
    return render_template('contacto.html')

#Ejecucion de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)