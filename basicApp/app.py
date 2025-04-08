from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "hello, Flask, This is the home page"


@app.route('/about')
def about():
    return "This is the about page"

if __name__ == "__main__":
    app.run(debug=True)
