from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
import os

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        path = self.url().path

        if path == "/":  # Si es la ruta raíz (home page)
            self.serve_home_page()
        elif path.startswith("/proyecto"):  # Si es la ruta de proyectos
            self.serve_project_page()
        else:
            self.serve_404_page()

    def serve_home_page(self):
        try:
            with open("home.html", "r", encoding="utf-8") as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        
        except FileNotFoundError:
            self.serve_404_page()

    def serve_project_page(self):
        query = self.query_data()
        partes_path = self.url().path.lstrip("/").split("/")
        
        if len(partes_path) >= 2 and partes_path[0] == "proyecto":
            proyecto = partes_path[1]  # Extraer el nombre del proyecto
        else:
            proyecto = "desconocido"

        autor = query.get("autor", "anónimo")  # Obtener el autor o "anónimo"

        content = f"""
        <h1>Proyecto: {proyecto} Autor: {autor}</h1>
        <p>URL Parse Result: {self.url()}</p>
        <p>Path Original: {self.path}</p>
        <p>Headers: {self.headers}</p>
        <p>Query: {self.query_data()}</p>
        """
        
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def serve_404_page(self):
        content = """
        <h1>Error 404: Página no encontrada</h1>
        <p>La página solicitada no existe.</p>
        """
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
