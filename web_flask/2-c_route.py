#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Route: / - displays "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route: /hbnb - displays "HBNB"
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'

# Route: /c/<text> - displays "C " followed by the value of the text variable
# (replace underscore _ symbols with a space)
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    # Replace underscores with spaces in the provided text
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
