
from sqlalchemy import create_engine,text
import os
#added security to protect the password
db_connection_string = os.environ['db_connection']
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
