
#19th jan
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
        columns = ['id', 'title', 'location', 'salary','currency','responsibility','requirements']
         # Access columns using names or indices, tuple doesn't take string values to map
        values = [row[i] for i in range(len(columns))]
       
        
        
        return(values)
        
        
