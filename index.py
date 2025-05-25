# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query = parse_qs(parsed_url.query)
        names = query.get("name", [])

        result = [marks_data.get(name, None) for name in names]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # CORS
        self.end_headers()

        response = json.dumps({"marks": result})
        self.wfile.write(response.encode())
