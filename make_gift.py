"""Run the gift website locally with Python: python make_gift.py"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser

HOST, PORT = "127.0.0.1", 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
url = f"http://{HOST}:{PORT}"
print(f"Your gift is ready at {url}")
print("Press Ctrl+C to stop the local preview.")
try:
    webbrowser.open(url)
except Exception:
    pass
ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler).serve_forever()
