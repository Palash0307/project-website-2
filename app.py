from flask import Flask,render_template

app =Flask(__name__)
# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
