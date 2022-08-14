# Type ctrl+shift+p to pull up Command Pallate
# type 'Python: Select Interpreter' and then select PythonData

# Import dependencies
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

# Create the app root (starting point)
@app.route('/')
def hello_world():
    return 'Hello world'