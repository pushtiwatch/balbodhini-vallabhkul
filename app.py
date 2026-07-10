import os
import json
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/timeline')
def get_timeline():
    json_path = os.path.join(os.path.dirname(__file__), 'timeline_data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "timeline_data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding timeline_data.json"}), 500

@app.route('/assets/evidence/<path:filename>')
def serve_evidence(filename):
    evidence_dir = os.path.join(app.root_path, 'assets', 'evidence')
    
    # 1. Try exact match first
    if os.path.exists(os.path.join(evidence_dir, filename)):
        return send_from_directory(evidence_dir, filename)
        
    # 2. Try normalized case and separator (hyphen/underscore) matching
    normalized_target = filename.lower().replace('_', '-').replace(' ', '-')
    try:
        for existing_file in os.listdir(evidence_dir):
            normalized_existing = existing_file.lower().replace('_', '-').replace(' ', '-')
            if normalized_existing == normalized_target:
                return send_from_directory(evidence_dir, existing_file)
    except OSError:
        pass
        
    # Fallback to standard handler
    return send_from_directory(evidence_dir, filename)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
