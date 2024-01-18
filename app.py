from flask import Flask,render_template,jsonify

app =Flask(__name__)
JOBS=[{
    'id':1,
    'title':'Data Analyst',
    'location':'Delhi India',
    'salary':'Rs. 10,00,000'
},
{
    'id':2,
    'title':'Data Science',
    'location':'Delhi India',
    'salary':'Rs. 15,00,000'

},
{
    'id':3,
    'title':'Data engineer',
    'location':'Delhi India',
    'salary':'Rs. 15,00,000'

}
]
# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS,company_name='Palash')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
