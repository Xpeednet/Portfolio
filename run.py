#Importar componentes
from flask import Flask

#Crear app medante instancia de clase Flask
app=Flask(__name__)

#Rutas de la aplicación
@app.route('/', methods=['GET'])
def holamundo():
    return 'Hola Mundo'

@app.route('/misproyectos')
def misproyectos():
    return 'Mis proyectos'

#Ejecucion de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)