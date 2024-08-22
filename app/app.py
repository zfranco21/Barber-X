from flask import Flask, render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)

# Configurar la base de datos MySQL en Hostinger
app.config['MYSQL_HOST'] = 'red-rail-734138.hostingersite.com'   # Reemplaza con tu host en Hostinger
app.config['MYSQL_USER'] = 'u653663436_root'      # Reemplaza con el nombre de usuario que creaste
app.config['MYSQL_PASSWORD'] = 'Proyectowebs1'  # Reemplaza con la contraseña que configuraste
app.config['MYSQL_DATABASE'] = 'u653663436_barberx'  # Reemplaza con el nombre de tu base de datos

# Inicialización de MySQL
mysql = MySQL(app)

# Rutas de la aplicación
@app.route('/')
def index():
    # Ejemplo de uso de la base de datos: obtener datos de la tabla 'roles'
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    cursor.close()
    return render_template('index.html', roles=roles)

if __name__ == '__main__':
    app.run(debug=True)
