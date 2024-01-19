from flask import Flask,render_template,jsonify
from sqlalchemy import text
from database import load_jobs_from_db
app =Flask(__name__)
jobsdb=load_jobs_from_db()
# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return render_template('home.html',jobs=jobsdb,company_name='Palash')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobsdb)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
