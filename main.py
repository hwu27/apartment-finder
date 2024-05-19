import functions_framework
import google.cloud.logging
import logging
from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
from flask import Flask

def check_availability(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")

    elements = soup.find_all('h2')
    pattern = re.compile(r"3 Bed", re.IGNORECASE)

    client = google.cloud.logging.Client()
    handler = CloudLoggingHandler(client)
    setup_logging(handler)
    
    for element in elements:
        if pattern.search(element.get_text()):
            logging.critical(f"Available apartment found: {url}", extra={
                "labels": {
                    "url": url,
                    "status": "Available"
                }
            })
            return "Available"
        logging.info(f"Not found: {url}", extra={
        "labels": {
            "url": url,
            "status": "Not found"
        }
    })
    return "Not found"

@functions_framework.http
def handle_req(request):
    request_json = request.get_json(silent=True)
    if not request_json or 'urls' not in request_json:
        logging.error({'error': 'Invalid input'})
        return json.dumps({'error': 'Invalid input'}), 400

    urls = request_json.get("urls", [])
    results = {}
    for url in urls:
        try:
            results[url] = check_availability(url)
        except Exception as e:
            results[url] = f"Error: {str(e)}"
            logging.error(f"Error: {str(e)}")

    return json.dumps(results), 200

app = Flask(__name__)

if __name__ == '__main__':
    # start the local server
    app.run(host='0.0.0.0', port=8080)