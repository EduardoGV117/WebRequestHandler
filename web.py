from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# Contenido completo de las páginas HTML almacenadas en memoria
contenido = {
    '/': """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mi Servidor Web </title>
    <link href="css/style.css" rel="stylesheet">
  </head>
  <body>
    <h1>Mi proyecto servidor web </h1> 
    <h3>
      soy un programador y estudiante del instituto tecnologico de tijuana presentando mi proyecto que es un servidor web http
    </h3>
    <h2>Proyectos</h2>
    <h3><a href="/proyecto/1"> Web Estática  - App de recomendación de libros </a></h3>
    <h3><a href="/proyecto/2"> Web App - MeFalta, qué película o serie me falta ver </a></h3>
    <h3><a href="/proyecto/3"> Web App - Foto22,  web para gestión de fotos </a></h3>
    <h2>Experiencia</h2>
    <h3>Desarrolladora Web Freelance</h3>
    <h3>Backend: FastAPI, nodejs, Go</h3>
    <h3>Frontend: JavaScript, htmx, React</h3>
  </body>
</html>
    """,
    '/proyecto/1': """<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Ana Lee</title>
    <link href="css/style.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Ana Lee</h1>
    <h2>Recomendación de libros</h2>
    <p>
      El proyecto consiste en el diseño de un sitio que muestra la información
      de distintos libros. La información se obtiene de una base de datos que se
      actualiza cada vez que se agrega un nuevo libro. Lorem ipsum dolor sit
      amet, consectetur adipiscing elit.
    </p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>Redis</li>
    </ul>
  </body>
</html>
    """
}

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        # Verificar si la ruta existe en el diccionario
        if path in contenido:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            # Enviar el contenido HTML almacenado
            self.wfile.write(contenido[path].encode("utf-8"))
        else:
            self.send_404()

    def send_404(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        content = "<h1>Error 404: Página no encontrada</h1>"
        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
