
from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://zf0v4i9mr77bkrkbhqnd:pscale_pw_CpF8hNUCzzMwQZgFlYe6Zqd2Xi1x3foKBajDy4WObzp@aws.connect.psdb.cloud/project_recruit_db?charset=utf8mb4",
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
