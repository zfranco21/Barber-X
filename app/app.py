from flask import Flask, render_template

app = Flask(__name__)

# Configurar la base de datos MySQL en Hostinger

# Inicialización de mysqldb



# Rutas de la aplicación

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)