#!/usr/bin/env python3
"""Local preview server for the ZWISCHENWELTEN website.

GitHub Pages serves clean URLs (/aktuelles -> aktuelles.html) automatically.
Plain static servers and file:// cannot, so use this for local previews:

    python3 dev-server.py

Then open http://localhost:8000
"""
import http.server
import os

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        resolved = super().translate_path(path)
        if not os.path.exists(resolved) and os.path.exists(resolved + ".html"):
            return resolved + ".html"
        return resolved


if __name__ == "__main__":
    print(f"Serving on http://localhost:{PORT} (Ctrl+C to stop)")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), CleanUrlHandler).serve_forever()
