#!/usr/bin/env python3
"""
Sudarshan Web Interface Launcher
Simple launcher for the web version of Sudarshan
"""

import sys
import os
import subprocess

def main():
    print("""
    
    SUDARSHAN AI SECURITY SCANNER - WEB INTERFACE
    Professional Edition Web Application
    
    Starting web server...
    Access at: http://localhost:5000
    
    """)
    
    try:
        # Check if Flask is installed
        import flask
        print("✓ Flask found")
        
        # Start the web application
        from web_app import app
        print("✓ Starting web server on http://localhost:5000")
        print("✓ Press Ctrl+C to stop")
        
        app.run(debug=False, host='0.0.0.0', port=5000)
        
    except ImportError:
        print("❌ Flask not found. Installing dependencies...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_web.txt'])
        print("✓ Dependencies installed. Please run again.")
        return 1
    except KeyboardInterrupt:
        print("\n✓ Web server stopped")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())