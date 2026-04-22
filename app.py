# Importamos Flask para crear la app web,
# render_template para enviar datos al HTML,
# request para capturar datos del formulario
from flask import Flask, render_template, request

# Importamos nuestra función de scraping
from scraper import get_instagram_data

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal "/" que acepta GET (mostrar página)
# y POST (cuando el usuario envía el formulario)
@app.route("/", methods=["GET", "POST"])
def index():
    # Variables para almacenar resultados o errores
    data = None
    error = None

    # Si el usuario envía el formulario
    if request.method == "POST":
        # Obtenemos los datos del formulario
        username = request.form.get("username")
        link = request.form.get("link")

        # Tomamos el username o el link (el que esté lleno)
        input_value = username if username else link

        # Si hay algún valor ingresado
        if input_value:
            # Llamamos a la función de scraping
            data = get_instagram_data(input_value)

            # Si falla la extracción, mostramos error
            if not data:
                error = "No se pudo obtener información. Asegúrate de que el usuario exista o intenta en unos minutos."

    # Renderizamos el HTML y enviamos los datos o error
    return render_template("index.html", data=data, error=error)

# Ejecutamos la app en modo debug (para desarrollo)
if __name__ == "__main__":
    app.run(debug=True)