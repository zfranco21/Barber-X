from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configurar la base de datos MySQL en Hostinger
db_config = {
    'host': 'red-rail-734138.hostingersite.com',          # Reemplaza con tu host en Hostinger
    'user': 'u653663436_root',             # Reemplaza con el nombre de usuario que creaste
    'password': 'Proyectowebs1',      # Reemplaza con la contraseña que configuraste
    'database': 'u653663436_barberx'   # Reemplaza con el nombre de tu base de datos
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rutas de la aplicación
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', roles=roles)

if __name__ == '__main__':
    app.run(debug=True)
