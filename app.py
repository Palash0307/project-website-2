from flask import Flask,render_template,jsonify,request
from sqlalchemy import text
from database import load_jobs_from_db,load_job_from_db,add_application_to_db
app =Flask(__name__)
jobsdb=load_jobs_from_db()
# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return render_template('home.html',jobs=jobsdb)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobsdb)
@app.route("/job/<id>")
def show_job(id):
    job=load_job_from_db(id)
    if not job:
        return "Not Found",404
    # will extract the data from job and will put in jobpage.html
    return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply",methods=['GET','POST'])

# Store this in the database
# Display an acknowledgment, to show the template after receiving from application_form which is taken by request.form
        
def apply_to_job(id):
    if request.method == 'POST':
        # Handling POST request
        data = request.form
        job = load_job_from_db(id)
        add_application_to_db(id, data)
        # Store this in the database
        # Display an acknowledgment, to show the template after receiving from application_form which is taken by request.form
        return render_template('application_submit.html', application=data, job=job)
    elif request.method == 'GET':
        # Handling GET request
        job = load_job_from_db(id)
        return render_template('application_submit.html', application=data,job=job)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
