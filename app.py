from flask import Flask, render_template
import os

app = Flask(__name__)

# Configure Flask based on environment
# Use environment variable to control debug mode (safer for production)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/careers')
def Careers():
    return render_template('career.html')


if __name__ == '__main__':
    # Use environment variables for configuration
    # Default to development settings for local testing
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    # Use 0.0.0.0 and port 5000 for Replit environment
    # This allows the Replit proxy to properly route traffic
    app.run(host=host, port=port, debug=debug)
