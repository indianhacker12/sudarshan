#!/usr/bin/env python3
"""
Sudarshan AI Security Scanner - Web Interface
Flask-based web application for the Sudarshan security scanner
"""

from flask import Flask, render_template, request, jsonify, session
import subprocess
import threading
import time
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sudarshan_security_scanner_2025'

# Global variables for scan status
scan_status = {}
scan_results = {}

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def start_scan():
    """Start a security scan"""
    data = request.get_json()
    target_url = data.get('url')
    scan_mode = data.get('mode', 'medium')
    verbose = data.get('verbose', False)
    
    if not target_url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Generate scan ID
    scan_id = f"scan_{int(time.time())}"
    
    # Initialize scan status
    scan_status[scan_id] = {
        'status': 'running',
        'progress': 0,
        'start_time': datetime.now().isoformat(),
        'url': target_url,
        'mode': scan_mode
    }
    
    # Start scan in background thread
    thread = threading.Thread(target=run_scan, args=(scan_id, target_url, scan_mode, verbose))
    thread.daemon = True
    thread.start()
    
    return jsonify({'scan_id': scan_id, 'status': 'started'})

@app.route('/scan/<scan_id>/status')
def get_scan_status(scan_id):
    """Get scan status and progress"""
    if scan_id not in scan_status:
        return jsonify({'error': 'Scan not found'}), 404
    
    return jsonify(scan_status[scan_id])

@app.route('/scan/<scan_id>/results')
def get_scan_results(scan_id):
    """Get scan results"""
    if scan_id not in scan_results:
        return jsonify({'error': 'Results not found'}), 404
    
    return jsonify(scan_results[scan_id])

def run_scan(scan_id, target_url, scan_mode, verbose):
    """Run the actual security scan"""
    try:
        # Update status
        scan_status[scan_id]['status'] = 'running'
        scan_status[scan_id]['progress'] = 10
        
        # Build command based on scan mode
        if scan_mode == 'basic':
            cmd = ['python', 'fast_scan.py', '-u', target_url]
        elif scan_mode == 'aggressive':
            cmd = ['python', 'main.py', '-u', target_url, '--owasp-all', '--chain-attacks']
        else:  # medium
            cmd = ['python', 'main.py', '-u', target_url, '--owasp-all']
        
        if verbose:
            cmd.append('--verbose')
        
        # Update progress
        scan_status[scan_id]['progress'] = 30
        
        # Run the scan
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)  # 30 min timeout
        
        # Update progress
        scan_status[scan_id]['progress'] = 90
        
        # Store results
        scan_results[scan_id] = {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode,
            'end_time': datetime.now().isoformat()
        }
        
        # Update final status
        scan_status[scan_id]['status'] = 'completed' if result.returncode == 0 else 'failed'
        scan_status[scan_id]['progress'] = 100
        scan_status[scan_id]['end_time'] = datetime.now().isoformat()
        
    except subprocess.TimeoutExpired:
        scan_status[scan_id]['status'] = 'timeout'
        scan_status[scan_id]['progress'] = 100
        scan_results[scan_id] = {'error': 'Scan timed out after 30 minutes'}
    except Exception as e:
        scan_status[scan_id]['status'] = 'error'
        scan_status[scan_id]['progress'] = 100
        scan_results[scan_id] = {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)