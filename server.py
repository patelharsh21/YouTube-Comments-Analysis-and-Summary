# from flask import Flask, request, jsonify
# import sys 
# sys.path.append("/home/harsh-patel/Desktop/projects/comments-summary-ml-project-main")
# import app
# from  app import get_summary_from_url  # Assuming your function is in a module named your_module
# from flask_cors import CORS


# app = Flask(__name__)
# CORS(app)
# @app.route('/summarize', methods=['GET'])
# def summarize():
#     url = request.args.get('url')
#     summary = get_summary_from_url(url)
#     return jsonify({'summary': summary})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys 
sys.path.append("/home/harsh-patel/Desktop/projects/comments-summary-ml-project-main")
from app import get_summary_from_url  # Assuming your function is in a module named your_module

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    url = data.get('url')
    summary = get_summary_from_url(url)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)