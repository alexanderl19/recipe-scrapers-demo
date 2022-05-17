from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs
from recipe_scrapers import scrape_me
import json


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        recipe_url = parse_qs(parsed_url.query)['url'][0]
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        scraper = scrape_me(recipe_url)
        response = {
            "title": scraper.title(),
            "total_time": scraper.total_time(),
            "yields": scraper.yields(),
            "ingredients": scraper.ingredients(),
            "instructions": scraper.instructions(),
            "image": scraper.image(),
            "host": scraper.host(),
            "links": scraper.links(),
            "nutrients": scraper.nutrients()
        }
        self.wfile.write(json.dumps(response).encode())
        return
