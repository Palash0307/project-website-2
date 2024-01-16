from flask import Flask

app =Flask(__name__)
# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
