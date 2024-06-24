from flask import Flask

app = Flask(__name__)

@app.route("/")
def hari():
    return 'Welcome'

app.run('0.0.0.0')