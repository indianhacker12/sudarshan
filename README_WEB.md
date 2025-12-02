# SUDARSHAN Web Interface

## Quick Start

### 1. Install Web Dependencies
```bash
pip install -r requirements_web.txt
```

### 2. Launch Web Interface
```bash
python sudarshan.py --web
```

### 3. Access Web Interface
Open your browser and go to: `http://localhost:5000`

## Features

- **Modern Web UI**: Clean, responsive interface
- **Real-time Progress**: Live scan progress updates
- **Three Scan Modes**: Basic, Medium, Aggressive
- **AI Integration**: Same LLaMA 3.2 AI analysis
- **Remote Access**: Access from any device on network

## Usage

1. Enter target URL
2. Select scan mode:
   - **Basic**: Fast vulnerability detection
   - **Medium**: OWASP Top 10 + AI analysis (recommended)
   - **Aggressive**: Deep testing + chain attacks
3. Click "Start Scan"
4. Monitor real-time progress
5. View detailed results

## Network Access

To allow access from other devices:
```bash
python web_app.py  # Runs on 0.0.0.0:5000
```

## Security Notes

- Web interface runs locally by default
- Same security scanning capabilities as desktop version
- All legal disclaimers apply
- Only scan authorized targets

## Troubleshooting

### Flask Not Found
```bash
pip install Flask==2.3.3
```

### Port Already in Use
Change port in `web_app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```