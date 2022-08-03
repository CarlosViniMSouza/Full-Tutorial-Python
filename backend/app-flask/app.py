from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<h2> Hello Flask! </h2>"

# execute the command in bash terminal: flask run