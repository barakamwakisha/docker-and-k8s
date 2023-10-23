import os
from flask import Flask

app = Flask(__name__)

# Get the value of the NAME environment variable or use 'ANON' as a default
name = os.environ.get('NAME', 'ANON')

@app.route('/')
def hello():
    return f"Hello, {name} from Flask!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)