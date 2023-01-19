from flask import Flask
app = Flask(__name__)
@app.route('/')
def i_love_nick():
    return 'I love Nick'