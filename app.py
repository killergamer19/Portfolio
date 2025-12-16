from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
FLOWISE_API_URL = os.getenv('FLOWISE_API_URL', 'http://localhost:3000')
FLOWISE_CHATFLOW_ID = os.getenv('FLOWISE_CHATFLOW_ID', '')

# Flowise API Configuration
FLOWISE_PREDICTION_URL = os.getenv('FLOWISE_PREDICTION_URL', 'https://cloud.flowiseai.com/api/v1/prediction/b64b685f-68e5-455d-b71b-5818bbb03f4b')

def query(payload):
    """Query the Flowise API"""
    response = requests.post(FLOWISE_PREDICTION_URL, json=payload)
    return response.json()

@app.route('/')
def index():
    """Render the main portfolio page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat requests and forward them to Flowise
    """
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = query({
            "question": message
        })
        
        if response:
            return jsonify(response)
        
        else:
            return jsonify({'error': 'Flowise API error'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
