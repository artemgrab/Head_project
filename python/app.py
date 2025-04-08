import os
import httpx
import subprocess
from flask import Flask, render_template, jsonify, url_for, request

app = Flask("voice_app")
script_process = None

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return "index.html not found", 404

@app.route("/edu")
def edu():
    try:
        return render_template("edu.html")
    except Exception as e:
        return "edu.html not found", 404

@app.route("/qa")
def qa():
    try:
        return render_template("q&a.html")
    except Exception as e:
        return "q&a.html not found", 404
    
@app.route("/test")
def test():
    try:
        return render_template("test.html")
    except Exception as e:
        return "test.html not found", 404

@app.route("/toggle_script", methods=['POST'])
def toggle_script():
    global script_process
    if request.json.get('action') == 'start':
        if script_process is None:
            script_process = subprocess.Popen(['../venv/bin/python', 'main.py'])
            return jsonify({'status': 'started'})
    elif request.json.get('action') == 'stop':
        if script_process is not None:
            script_process.terminate()
            script_process = None
            return jsonify({'status': 'stopped'})
    return jsonify({'status': 'unchanged'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8116, debug=True)
