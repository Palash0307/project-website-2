
from sqlalchemy import create_engine,text
import os
db_connection_string=os.environ('db_connection_string')
engine = create_engine(db_connection_string,
                    connect_args={"ssl": {
                                            "ssl_ca":"/etc/ssl/cert.pem",
                                            
                                        }
                                    }
                                )

def load_jobs_from_db():
    with engine.connect() as conn:
        result=conn.execute(text("Select * from jobs"))
        jobs=[]
        for row in result.all():
            #cinverting legacy row into dicts
            jobs.append(row._mapping)
        return jobs
