from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/home')
def index():
    return 'Hello World! Welcome to my Home Page!'

@app.route('/about')
def about():
    name = "Ariana"
    location = "Akron/Warren/Youngstown"
    return f"My name is {name}, and I provide services in the {location} area."

@app.route('/contact')
def contact():
    email = "adavis@gmail.com"
    return f"Questions? Please reach out to {email}."

if __name__ == "__main__":
    app.run(debug=True)

