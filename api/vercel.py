from flask import Flask, request, jsonify
from flask_cors import CORS
from vercel_wsgi import handler
import sys
import os

# Adjust the path if necessary
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from utils import get_summary_from_url  # Ensure utils.py has get_summary_from_url

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    url = data.get('url')
    summary = get_summary_from_url(url)
    return jsonify({'summary': summary})

# The handler for Vercel
def handler_function(event, context):
    return handler(app, event, context)
