from flask import Flask, render_template
import os

app = Flask(__name__)

# Configure Flask for Replit environment
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # Use 0.0.0.0 and port 5000 for Replit environment
    # This allows the Replit proxy to properly route traffic
    app.run(host='0.0.0.0', port=5000, debug=True)