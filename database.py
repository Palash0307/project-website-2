
#19th jan
from flask import request
from sqlalchemy import create_engine,text
import os
#added security to protect the password
db_connection_string = os.environ['db_connection'] #name to be added in environment 19thjan
engine = create_engine(db_connection_string,
                    connect_args={"ssl": { #to get from clouddb sources
                                            "ssl_ca":"/etc/ssl/cert.pem",
                                            
                                        }
                                    }
                                )

def load_jobs_from_db():
    with engine.connect() as conn:
        result=conn.execute(text("Select * from jobs"))
        jobs=[]
        for row in result.all():
            #converting legacy row into dicts
            jobs.append(row._mapping)
            
        return jobs
#to execute a specific job details
def load_job_from_db(id):
    with engine.connect() as conn:
        #val to show the id to be placed
        result=conn.execute(text("Select * from jobs where id = :val").bindparams(val=id))
        row = result.fetchone()
        if row:
            columns = ['id', 'title', 'location', 'salary', 'currency', 'responsibility', 'requirements']
            # Access columns using names or indices, tuple doesn't take string values to map
            values = [row[i] for i in range(len(columns))]
            return dict(zip(columns, values))
        else:
            return None
       
        
        
        
def add_application_to_db(id,application):
    print(application)
#going to retreive the data from our apply_to_job function in which the data object is taking our application inputs from application_submit which is linked to application_form
    with engine.connect() as conn:

        query = text("""
        INSERT INTO Applications (job_id,full_name, email, linkedin_url, education, work_experience, resume_url)
        VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
        """).bindparams(job_id=id,
                     full_name=request.form.get('full_name', ''),
                     email=request.form.get('email', ''),
                     linkedin_url=request.form.get('linkedin_url', ''),
                     work_experience=request.form.get('experience', ''),
                     education=request.form.get('education', ''),
                     resume_url=request.form.get('resume_url', ''),)
        conn.execute(query)
                     
        
        
