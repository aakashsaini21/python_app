from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)