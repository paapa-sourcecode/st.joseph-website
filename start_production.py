#!/usr/bin/env python3
"""
Production startup script for Flask application.
This script sets up environment variables for production deployment.
"""

import os
import subprocess
import sys

def set_production_environment():
    """Set production environment variables"""
    os.environ.setdefault('FLASK_DEBUG', 'false')
    os.environ.setdefault('FLASK_ENV', 'production')
    os.environ.setdefault('FLASK_HOST', '0.0.0.0')
    os.environ.setdefault('FLASK_PORT', '5000')
    
    print("Production environment variables set:")
    print(f"  FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")
    print(f"  FLASK_ENV: {os.environ.get('FLASK_ENV')}")
    print(f"  FLASK_HOST: {os.environ.get('FLASK_HOST')}")
    print(f"  FLASK_PORT: {os.environ.get('FLASK_PORT')}")

def start_gunicorn():
    """Start the application with gunicorn"""
    print("\nStarting Flask application with gunicorn...")
    try:
        subprocess.run([
            'gunicorn', 
            '-c', 'gunicorn_config.py', 
            'app:app'
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting gunicorn: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        sys.exit(0)

if __name__ == '__main__':
    set_production_environment()
    start_gunicorn()