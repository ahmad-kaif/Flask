from flask import Flask
# This is a simple Flask application with two routes: home and about.
app = Flask(__name__)

# The home route returns a simple message.
@app.route('/')
def home():
    return "hello, Flask, This is the home page"


# The about route returns a simple message.


@app.route('/about')
def about():
    return "This is the about page"

if __name__ == "__main__":
    app.run(debug=True)
