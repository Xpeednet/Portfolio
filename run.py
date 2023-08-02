#Importar componentes
from flask import Flask, render_template, request

#Crear app medante instancia de clase Flask
app=Flask(__name__)

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

@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template('/contacto.html')

#Ejecucion de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)